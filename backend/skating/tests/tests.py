from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from ..models import Element, Skater, Result, ElementCode, Level


class SkateBackendTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.admin_user = User.objects.create_superuser(
            'admin', 'admin@test.com', 'pass123'
        )

        self.skater_user = User.objects.create_user(
            'mabel', 'mabel@test.com', 'pass123'
        )

        self.element = Element.objects.create(
            name=ElementCode.TRAVELING,
            level=Level.ONE,
            base_score=2.00,
            extra_points=0.5,
            qoe_1=0.5,
            qoe_2=1.0,
            qoe_3=1.5
        )

        self.skater_admin = Skater.objects.create(
            name="Admin Skater", user=self.admin_user
        )

        self.skater_mabel = Skater.objects.create(
            name="Mabel", user=self.skater_user
        )

    def test_total_score_calculation(self):
        """Verifica que BV + Extra + QOE sea correcto"""
        result = Result.objects.create(
            skater=self.skater_mabel,
            element=self.element,
            qoe_given=2
        )

        self.assertEqual(result.total_score, 3.5)

    def test_skater_privacy_results(self):
        """Un patinador NO debe ver resultados de otros"""
        Result.objects.create(skater=self.skater_admin, element=self.element)

        self.client.force_authenticate(user=self.skater_user)
        response = self.client.get('/api/results/')

        self.assertEqual(len(response.data), 0)

    def test_stats_endpoint_structure(self):
        """Verifica que el endpoint de estadísticas sirva lo que el Radar
        necesita"""
        Result.objects.create(
            skater=self.skater_mabel, element=self.element, qoe_given=1
        )

        self.client.force_authenticate(user=self.skater_user)
        response = self.client.get(
            f'/api/skaters/{self.skater_mabel.id}/stats/'
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.data[0]['element__name'], ElementCode.TRAVELING
        )
        self.assertTrue('average' in response.data[0])

    def test_admin_can_manage_elements(self):
        """Solo admin puede crear elementos en el catálogo"""
        self.client.force_authenticate(user=self.skater_user)
        response = self.client.post(
            '/api/elements/', {'name': 'ASq', 'base_score': 5.0}
        )
        self.assertEqual(response.status_code, 403)
