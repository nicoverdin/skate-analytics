from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Skater, Element, Result


class ElementTests(APITestCase):
    def setUp(self):
        self.url = reverse('element-list')
        self.element_data = {
            'name': 'Tr',
            'level': 1,
            'base_score': 5.0,
            'extra_points': 1.5
        }

    def test_create_element(self):
        """Prueba crear un elemento técnico y que el código se genere solo"""
        response = self.client.post(self.url, self.element_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Element.objects.count(), 1)

        element = Element.objects.get()
        self.assertEqual(element.code, 'Tr1% (1.5)')

    def test_unique_code_constraint(self):
        """Prueba que NO se pueden crear dos elementos idénticos"""
        self.client.post(self.url, self.element_data, format='json')
        response = self.client.post(self.url, self.element_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_total_score_calculation(self):
        """Prueba que el serializer calcula base + extra correctamente"""
        response = self.client.post(self.url, self.element_data, format='json')
        self.assertEqual(response.data['total_score'], 6.5)


class SkaterTests(APITestCase):
    def setUp(self):
        self.url = reverse('skater-list')
        self.skater_data = {'name': 'Yuna Kim'}

    def test_create_skater(self):
        response = self.client.post(self.url, self.skater_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Skater.objects.get().name, 'Yuna Kim')

    def test_update_skater(self):
        """Prueba cambiar el nombre de un patinador"""
        skater = Skater.objects.create(name='Yuna Kim')
        url_detail = reverse('skater-detail', args=[skater.id])
        updated_data = {'name': 'Queen Yuna'}

        response = self.client.patch(url_detail, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        skater.refresh_from_db()
        self.assertEqual(skater.name, 'Queen Yuna')


class ResultIntegrationTests(APITestCase):
    """
    Aquí probamos la interacción entre Patinador, Elemento y Resultado.
    Es la parte más crítica de tu sistema.
    """
    def setUp(self):
        self.skater = Skater.objects.create(name='Javier Fernandez')
        self.element = Element.objects.create(
            name='Tr', level=4, base_score=10.0, extra_points=2.0
        )
        self.url = reverse('result-list')

    def test_create_result(self):
        """Prueba asignar un elemento a un patinador"""
        data = {
            'skater': self.skater.id,
            'element': self.element.id,
            'is_program': True,
            'notes': 'Great landing'
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Result.objects.count(), 1)

    def test_nested_serializer_optimization(self):
        """
        CRÍTICO: Verifica que al pedir un resultado, Django nos da
        los datos del elemento GRATIS (Nested Serializer).
        """
        Result.objects.create(skater=self.skater, element=self.element)

        response = self.client.get(self.url)

        result_data = response.data[0]
        self.assertIn('element_details', result_data)
        self.assertEqual(result_data['element_details']['code'], 'Tr4% (2.0)')
        self.assertEqual(result_data['element_details']['total_score'], 12.0)

    def test_skater_total_score_logic(self):
        """
        CRÍTICO: Verifica que la API de Patinadores suma automáticamente
        los puntos de todos sus resultados.
        """
        Result.objects.create(skater=self.skater, element=self.element)
        Result.objects.create(skater=self.skater, element=self.element)

        url_skater = reverse('skater-list')
        response = self.client.get(url_skater)

        javier_data = response.data[0]

        self.assertEqual(float(javier_data['total_score']), 24.0)
        self.assertEqual(javier_data['elements_count'], 2)
