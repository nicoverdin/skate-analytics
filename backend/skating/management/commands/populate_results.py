import random
from django.core.management.base import BaseCommand
from skating.models import Skater, Element, Result


class Command(BaseCommand):
    help = 'Genera resultados de prueba para las patinadoras de la aplicación'

    def handle(self, *args, **options):
        nombres_patinadoras = [
            'Mabel Luengo', 'Alejandra López', 'Irene Aparicio',
            'Lucía Ostos', 'Martina Torres', 'María Gómez'
        ]

        elementos = list(Element.objects.all())

        if not elementos:
            self.stdout.write(self.style.ERROR('El catálogo está vacío. Ejecuta populate_elements primero.'))
            return

        self.stdout.write('Generando resultados de prueba...')

        for nombre in nombres_patinadoras:
            skater, created = Skater.objects.get_or_create(name=nombre)

            skater.results.all().delete()

            num_resultados = random.randint(3, 6)

            for _ in range(num_resultados):
                elemento_aleatorio = random.choice(elementos)
                qoe_aleatorio = random.randint(-3, 3)

                Result.objects.create(
                    skater=skater,
                    element=elemento_aleatorio,
                    qoe_given=qoe_aleatorio,
                    notes=f"Entrenamiento de {elemento_aleatorio.name}",
                    is_program=random.choice([True, False])
                )

        self.stdout.write(self.style.SUCCESS(f'Éxito: Se han generado resultados para {len(nombres_patinadoras)} patinadoras.'))
