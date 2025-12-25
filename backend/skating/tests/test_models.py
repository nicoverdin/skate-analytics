from django.test import TestCase
from ..models import Element, Result, Skater


class RollartLogicTest(TestCase):
    def setUp(self):
        self.skater = Skater.objects.create(name="Test Skater")
        # Creamos un Traveling Nivel 4 (Base 6.0, QOE3=1.5, Extra=0.5)
        self.element = Element.objects.create(
            name='Tr', level=4, base_score=6.0,
            qoe_1=0.5, qoe_2=1.0, qoe_3=1.5,
            extra_points=0.5
        )

    def test_calculation_with_positive_qoe(self):
        """6.0 (Base) + 1.0 (QOE+2) + 0.5 (Extra) = 7.5"""
        res = Result.objects.create(
            skater=self.skater, element=self.element, qoe_given=2
        )

        self.assertEqual(res.total_score, 7.5)

    def test_calculation_with_negative_qoe(self):
        """6.0 (Base) - 0.5 (QOE-1) + 0.5 (Extra) = 6.0"""
        res = Result.objects.create(
            skater=self.skater, element=self.element, qoe_given=-1
        )

        self.assertEqual(res.total_score, 6.0)

    def test_skater_average_score(self):
        # Creamos dos resultados: uno de 7.5 y otro de 4.5
        Result.objects.create(
            skater=self.skater, element=self.element, qoe_given=2
        )  # 7.5

        Result.objects.create(
            skater=self.skater, element=self.element, qoe_given=-3
        )  # 6-1.5+0.5 = 5.0

        # Media: (7.5 + 5.0) / 2 = 6.25
        total = sum(r.total_score for r in self.skater.results.all())
        avg = total / self.skater.results.count()
        self.assertEqual(avg, 6.25)
