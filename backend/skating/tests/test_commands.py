from django.core.management import call_command
from django.test import TestCase
from ..models import Element


class CommandsTest(TestCase):
    def test_populate_elements_command(self):
        """Verifica que el script carga los elementos y los QOE
        correctamente"""
        call_command('populate_elements')

        tr5 = Element.objects.get(name='Tr', level=5, extra_points='0.0')
        self.assertEqual(float(tr5.base_score), 6.5)
        self.assertEqual(float(tr5.qoe_3), 1.6)
        self.assertTrue(Element.objects.count() > 20)
