from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Skater, Element, Result


class BaseSkateTestCase(APITestCase):
    """
    Clase base para no repetir código.
    Crea un usuario y loguea al cliente automáticamente.
    """
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', password='password123'
        )

        self.client.force_authenticate(user=self.user)


class ElementTests(BaseSkateTestCase):
    def setUp(self):
        super().setUp()
        self.url = reverse('element-list')
        self.element_data = {
            'name': 'Tr',
            'level': 1,
            'base_score': 5.0,
            'extra_points': 1.5
        }

    def test_create_element(self):
        response = self.client.post(self.url, self.element_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        element = Element.objects.get()
        self.assertEqual(element.code, 'Tr1% (1.5)')

    def test_unique_code_constraint(self):
        self.client.post(self.url, self.element_data, format='json')
        response = self.client.post(self.url, self.element_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class SkaterTests(BaseSkateTestCase):
    def setUp(self):
        super().setUp()
        self.url = reverse('skater-list')
        self.skater_data = {'name': 'Yuna Kim'}

    def test_create_skater(self):
        response = self.client.post(self.url, self.skater_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        skater = Skater.objects.get(name='Yuna Kim')
        self.assertEqual(skater.user, self.user)

    def test_update_skater(self):
        skater = Skater.objects.create(name='Yuna Kim', user=self.user)
        url_detail = reverse('skater-detail', args=[skater.id])
        updated_data = {'name': 'Queen Yuna'}

        response = self.client.patch(url_detail, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        skater.refresh_from_db()
        self.assertEqual(skater.name, 'Queen Yuna')


class ResultIntegrationTests(BaseSkateTestCase):
    def setUp(self):
        super().setUp()
        # Importante: vincular el skater al usuario del test
        self.skater = Skater.objects.create(
            name='Javier Fernandez', user=self.user
        )

        self.element = Element.objects.create(
            name='Tr', level=4, base_score=10.0, extra_points=2.0
        )
        self.url = reverse('result-list')

    def test_create_result(self):
        data = {
            'skater': self.skater.id,
            'element': self.element.id,
            'is_program': True,
            'notes': 'Great landing'
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_nested_serializer_optimization(self):
        Result.objects.create(skater=self.skater, element=self.element)
        response = self.client.get(self.url)
        result_data = response.data[0]
        self.assertIn('element_details', result_data)
        self.assertEqual(result_data['element_details']['code'], 'Tr4% (2.0)')

    def test_skater_total_score_logic(self):
        Result.objects.create(skater=self.skater, element=self.element)
        Result.objects.create(skater=self.skater, element=self.element)

        url_skater = reverse('skater-list')
        response = self.client.get(url_skater)
        javier_data = response.data[0]

        self.assertEqual(float(javier_data['total_score']), 24.0)
        self.assertEqual(javier_data['elements_count'], 2)
