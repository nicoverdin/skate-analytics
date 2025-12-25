from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase
from ..models import Skater, Element, Result


class BaseSkateTestCase(APITestCase):
    """
    Clase base para autenticación y datos comunes.
    """
    def setUp(self):
        self.admin_user = User.objects.create_user(
            username='coach', password='password123', is_staff=True
        )

        self.normal_user = User.objects.create_user(
            username='skater_user', password='password123', is_staff=False
        )

        self.client.force_authenticate(user=self.admin_user)


class ElementAPITests(BaseSkateTestCase):
    def setUp(self):
        super().setUp()
        self.url = reverse('element-list')
        self.element_data = {
            'name': 'Tr',
            'level': 4,
            'base_score': 6.0,
            'qoe_1': 0.5,
            'qoe_2': 1.0,
            'qoe_3': 1.5,
            'extra_points': 0.5
        }

    def test_create_element_as_admin(self):
        """Solo staff puede añadir al catálogo"""
        response = self.client.post(self.url, self.element_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Element.objects.count(), 1)
        self.assertEqual(Element.objects.get().code, 'Tr3% (0.5)')

    def test_create_element_forbidden_for_normal_user(self):
        """Un usuario normal no puede modificar el catálogo"""
        self.client.force_authenticate(user=self.normal_user)
        response = self.client.post(self.url, self.element_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class SkaterAPITests(BaseSkateTestCase):
    def setUp(self):
        super().setUp()
        self.url = reverse('skater-list')
        self.skater = Skater.objects.create(
            name='Javier Fernandez', user=self.admin_user
        )

    def test_list_skaters_includes_average_score(self):
        """Verifica que la media que pide el componente Vue está presente"""
        el = Element.objects.create(name='ASq', level=1, base_score=5.0)
        Result.objects.create(
            skater=self.skater, element=el, qoe_given=0
        )  # Total: 5.0

        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('average_score', response.data[0])
        self.assertEqual(float(response.data[0]['average_score']), 5.0)


class ResultAPITests(BaseSkateTestCase):
    def setUp(self):
        super().setUp()
        self.skater = Skater.objects.create(
            name='Patinador Test', user=self.admin_user
        )

        self.element = Element.objects.create(
            name='Tr', level=4, base_score=6.0, qoe_2=1.0, extra_points=0.0
        )
        self.url = reverse('result-list')

    def test_create_result_calculates_total_correctly(self):
        """Verifica que al postear un resultado, el total es correcto"""
        data = {
            'skater': self.skater.id,
            'element': self.element.id,
            'qoe_given': 2,
            'is_program': False
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(float(response.data['total_score']), 7.0)

    def test_result_list_optimization(self):
        """Verifica que element_details (nested) se envía para el buscador de
        Vue"""
        Result.objects.create(skater=self.skater, element=self.element)
        response = self.client.get(self.url)
        self.assertIn('element_details', response.data[0])
        self.assertEqual(response.data[0]['element_details']['name'], 'Tr')

    def test_result_includes_nested_details(self):
        """
        Verifica que el serializer devuelve 'skater_details' y
        'element_details' tal como espera el frontend para mostrar nombres y
        códigos.
        """
        Result.objects.create(
            skater=self.skater, element=self.element, qoe_given=2
        )

        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        data = response.data[0]

        self.assertIn('skater_details', data)
        self.assertEqual(data['skater_details']['name'], self.skater.name)

        self.assertIn('element_details', data)
        self.assertEqual(data['element_details']['code'], self.element.code)

    def test_create_result_with_id_only(self):
        """
        Asegura que aunque enviemos detalles para lectura,
        la creación sigue funcionando enviando solo los IDs (PKs).
        """
        data = {
            'skater': self.skater.id,
            'element': self.element.id,
            'qoe_given': 1,
            'is_program': False
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
