from django.core.management.base import BaseCommand
from skating.models import Element


class Command(BaseCommand):
    help = 'Puebla la base de datos con los elementos de Solo Danza Rollart 2026'

    def handle(self, *args, **options):
        self.stdout.write('Eliminando elementos antiguos...')
        Element.objects.all().delete()

        elementos_data = [
            # --- TRAVELING ---
            {'name': 'Tr', 'level': 0, 'base': 0.0, 'q1': 0.0, 'q2': 0.0, 'q3': 0.0, 'extra_points': 0.0},
            {'name': 'Tr', 'level': 1, 'base': 2.5, 'q1': 0.3, 'q2': 0.6, 'q3': 0.9, 'extra_points': 0.0},
            {'name': 'Tr', 'level': 2, 'base': 3.5, 'q1': 0.3, 'q2': 0.6, 'q3': 0.9, 'extra_points': 0.0},
            {'name': 'Tr', 'level': 3, 'base': 4.5, 'q1': 0.4, 'q2': 0.8, 'q3': 1.2, 'extra_points': 0.0},
            {'name': 'Tr', 'level': 4, 'base': 6.0, 'q1': 0.5, 'q2': 1.0, 'q3': 1.5, 'extra_points': 0.0},
            {'name': 'Tr', 'level': 5, 'base': 6.5, 'q1': 0.6, 'q2': 1.1, 'q3': 1.6, 'extra_points': 0.0},
            {'name': 'Tr', 'level': 2, 'base': 3.5, 'q1': 0.3, 'q2': 0.6, 'q3': 0.9, 'extra_points': 1.0},
            {'name': 'Tr', 'level': 3, 'base': 4.5, 'q1': 0.4, 'q2': 0.8, 'q3': 1.2, 'extra_points': 1.0},
            {'name': 'Tr', 'level': 4, 'base': 6.0, 'q1': 0.5, 'q2': 1.0, 'q3': 1.5, 'extra_points': 1.0},
            {'name': 'Tr', 'level': 5, 'base': 6.5, 'q1': 0.6, 'q2': 1.1, 'q3': 1.6, 'extra_points': 1.0},
            {'name': 'Tr', 'level': 2, 'base': 3.5, 'q1': 0.3, 'q2': 0.6, 'q3': 0.9, 'extra_points': 1.1},
            {'name': 'Tr', 'level': 3, 'base': 4.5, 'q1': 0.4, 'q2': 0.8, 'q3': 1.2, 'extra_points': 1.1},
            {'name': 'Tr', 'level': 4, 'base': 6.0, 'q1': 0.5, 'q2': 1.0, 'q3': 1.5, 'extra_points': 1.1},
            {'name': 'Tr', 'level': 5, 'base': 6.5, 'q1': 0.6, 'q2': 1.1, 'q3': 1.6, 'extra_points': 1.1},
            {'name': 'Tr', 'level': 2, 'base': 3.5, 'q1': 0.3, 'q2': 0.6, 'q3': 0.9, 'extra_points': 1.3},
            {'name': 'Tr', 'level': 3, 'base': 4.5, 'q1': 0.4, 'q2': 0.8, 'q3': 1.2, 'extra_points': 1.3},
            {'name': 'Tr', 'level': 4, 'base': 6.0, 'q1': 0.5, 'q2': 1.0, 'q3': 1.5, 'extra_points': 1.3},
            {'name': 'Tr', 'level': 5, 'base': 6.5, 'q1': 0.6, 'q2': 1.1, 'q3': 1.6, 'extra_points': 1.3},
            {'name': 'Tr', 'level': 2, 'base': 3.5, 'q1': 0.3, 'q2': 0.6, 'q3': 0.9, 'extra_points': 1.7},
            {'name': 'Tr', 'level': 3, 'base': 4.5, 'q1': 0.4, 'q2': 0.8, 'q3': 1.2, 'extra_points': 1.7},
            {'name': 'Tr', 'level': 4, 'base': 6.0, 'q1': 0.5, 'q2': 1.0, 'q3': 1.5, 'extra_points': 1.7},
            {'name': 'Tr', 'level': 5, 'base': 6.5, 'q1': 0.6, 'q2': 1.1, 'q3': 1.6, 'extra_points': 1.7},
            {'name': 'Tr', 'level': 2, 'base': 3.5, 'q1': 0.3, 'q2': 0.6, 'q3': 0.9, 'extra_points': 2.0},
            {'name': 'Tr', 'level': 3, 'base': 4.5, 'q1': 0.4, 'q2': 0.8, 'q3': 1.2, 'extra_points': 2.0},
            {'name': 'Tr', 'level': 4, 'base': 6.0, 'q1': 0.5, 'q2': 1.0, 'q3': 1.5, 'extra_points': 2.0},
            {'name': 'Tr', 'level': 5, 'base': 6.5, 'q1': 0.6, 'q2': 1.1, 'q3': 1.6, 'extra_points': 2.0},

            # --- ART SEQ ---
            {'name': 'ASq', 'level': 0, 'base': 0.0, 'q1': 0.0, 'q2': 0.0, 'q3': 0.0, 'extra_points': 0.0},
            {'name': 'ASq', 'level': 1, 'base': 3.0, 'q1': 0.3, 'q2': 0.6, 'q3': 0.9, 'extra_points': 0.0},
            {'name': 'ASq', 'level': 2, 'base': 4.0, 'q1': 0.3, 'q2': 0.6, 'q3': 0.9, 'extra_points': 0.0},
            {'name': 'ASq', 'level': 3, 'base': 5.5, 'q1': 0.4, 'q2': 0.8, 'q3': 1.2, 'extra_points': 0.0},
            {'name': 'ASq', 'level': 4, 'base': 7.1, 'q1': 0.7, 'q2': 1.4, 'q3': 2.1, 'extra_points': 0.0},
            {'name': 'ASq', 'level': 5, 'base': 9.3, 'q1': 1.0, 'q2': 2.0, 'q3': 3.0, 'extra_points': 0.0},

            # --- DANCE STEP SEQ ---
            {'name': 'DSSq', 'level': 0, 'base': 0.0, 'q1': 0.0, 'q2': 0.0, 'q3': 0.0, 'extra_points': 0.0},
            {'name': 'DSSq', 'level': 1, 'base': 3.0, 'q1': 0.3, 'q2': 0.6, 'q3': 0.9, 'extra_points': 0.0},
            {'name': 'DSSq', 'level': 2, 'base': 4.0, 'q1': 0.3, 'q2': 0.6, 'q3': 0.9, 'extra_points': 0.0},
            {'name': 'DSSq', 'level': 3, 'base': 5.5, 'q1': 0.4, 'q2': 0.8, 'q3': 1.2, 'extra_points': 0.0},
            {'name': 'DSSq', 'level': 4, 'base': 7.1, 'q1': 0.7, 'q2': 1.4, 'q3': 2.1, 'extra_points': 0.0},
            {'name': 'DSSq', 'level': 5, 'base': 9.3, 'q1': 1.0, 'q2': 2.0, 'q3': 3.0, 'extra_points': 0.0},

            # --- FOOT SEQ ---
            {'name': 'FoSq', 'level': 0, 'base': 0.0, 'q1': 0.0, 'q2': 0.0, 'q3': 0.0, 'extra_points': 0.0},
            {'name': 'FoSq', 'level': 1, 'base': 4.0, 'q1': 0.3, 'q2': 0.6, 'q3': 0.9, 'extra_points': 0.0},
            {'name': 'FoSq', 'level': 2, 'base': 5.0, 'q1': 0.4, 'q2': 0.8, 'q3': 1.2, 'extra_points': 0.0},
            {'name': 'FoSq', 'level': 3, 'base': 6.5, 'q1': 0.5, 'q2': 1.0, 'q3': 1.5, 'extra_points': 0.0},
            {'name': 'FoSq', 'level': 4, 'base': 8.1, 'q1': 0.7, 'q2': 1.4, 'q3': 2.1, 'extra_points': 0.0},
            {'name': 'FoSq', 'level': 5, 'base': 10.3, 'q1': 1.0, 'q2': 2.0, 'q3': 3.0, 'extra_points': 0.0},

            # --- CLUSTER SEQ ---
            {'name': 'ClSq', 'level': 0, 'base': 0.0, 'q1': 0.0, 'q2': 0.0, 'q3': 0.0, 'extra_points': 0.0},
            {'name': 'ClSq', 'level': 1, 'base': 3.0, 'q1': 0.3, 'q2': 0.6, 'q3': 0.9, 'extra_points': 0.0},
            {'name': 'ClSq', 'level': 2, 'base': 4.0, 'q1': 0.4, 'q2': 0.8, 'q3': 1.2, 'extra_points': 0.0},
            {'name': 'ClSq', 'level': 3, 'base': 5.3, 'q1': 0.5, 'q2': 1.0, 'q3': 1.5, 'extra_points': 0.0},
            {'name': 'ClSq', 'level': 4, 'base': 6.9, 'q1': 0.7, 'q2': 1.4, 'q3': 2.1, 'extra_points': 0.0},
            {'name': 'ClSq', 'level': 5, 'base': 7.5, 'q1': 0.7, 'q2': 1.4, 'q3': 2.1, 'extra_points': 0.0},

            # --- 1 SET CLUSTER SEQ ---
            {'name': '1SClSq', 'level': 0, 'base': 0.0, 'q1': 0.0, 'q2': 0.0, 'q3': 0.0, 'extra_points': 0.0},
            {'name': '1SClSq', 'level': 1, 'base': 2.0, 'q1': 0.3, 'q2': 0.6, 'q3': 0.9, 'extra_points': 0.0},
            {'name': '1SClSq', 'level': 2, 'base': 2.7, 'q1': 0.4, 'q2': 0.8, 'q3': 1.2, 'extra_points': 0.0},
            {'name': '1SClSq', 'level': 3, 'base': 3.5, 'q1': 0.4, 'q2': 0.8, 'q3': 1.2, 'extra_points': 0.0},
            {'name': '1SClSq', 'level': 4, 'base': 4.6, 'q1': 0.4, 'q2': 0.8, 'q3': 1.2, 'extra_points': 0.0},
            {'name': '1SClSq', 'level': 5, 'base': 5.0, 'q1': 0.5, 'q2': 1.0, 'q3': 1.5, 'extra_points': 0.0},

            # --- CHOREO STEP ---
            {'name': 'ChStS', 'level': 0, 'base': 0.0, 'q1': 0.0, 'q2': 0.0, 'q3': 0.0, 'extra_points': 0.0},
            {'name': 'ChStS', 'level': 1, 'base': 3.0, 'q1': 0.2, 'q2': 0.4, 'q3': 0.6, 'extra_points': 0.0},

            # --- PATTERN SEQUENCES ---
            # --- QUICKSTEP ---
            {'name': 'QSS1', 'level': 0, 'base': 0.0, 'q1': 0.0, 'q2': 0.0, 'q3': 0.0, 'extra_points': 0.0},
            {'name': 'QSS1', 'level': 1, 'base': 0.9, 'q1': 0.1, 'q2': 0.2, 'q3': 0.3, 'extra_points': 0.0},
            {'name': 'QSS1', 'level': 2, 'base': 1.8, 'q1': 0.3, 'q2': 0.6, 'q3': 0.9, 'extra_points': 0.0},
            {'name': 'QSS1', 'level': 3, 'base': 2.6, 'q1': 0.3, 'q2': 0.6, 'q3': 0.9, 'extra_points': 0.0},
            {'name': 'QSS1', 'level': 4, 'base': 3.8, 'q1': 0.3, 'q2': 0.6, 'q3': 0.9, 'extra_points': 0.0},
            {'name': 'QSS1', 'level': 5, 'base': 5.0, 'q1': 0.4, 'q2': 0.8, 'q3': 1.2, 'extra_points': 0.0},

            # --- TERENZI WALTZ ---
            {'name': 'TW1', 'level': 0, 'base': 0.0, 'q1': 0.0, 'q2': 0.0, 'q3': 0.0, 'extra_points': 0.0},
            {'name': 'TW1', 'level': 1, 'base': 1.0, 'q1': 0.1, 'q2': 0.2, 'q3': 0.3, 'extra_points': 0.0},
            {'name': 'TW1', 'level': 2, 'base': 2.0, 'q1': 0.3, 'q2': 0.6, 'q3': 0.9, 'extra_points': 0.0},
            {'name': 'TW1', 'level': 3, 'base': 2.6, 'q1': 0.3, 'q2': 0.6, 'q3': 0.9, 'extra_points': 0.0},
            {'name': 'TW1', 'level': 4, 'base': 3.2, 'q1': 0.3, 'q2': 0.6, 'q3': 0.9, 'extra_points': 0.0},
            {'name': 'TW1', 'level': 5, 'base': 4.0, 'q1': 0.3, 'q2': 0.6, 'q3': 0.9, 'extra_points': 0.0},

            # --- ITALIAN FOXTROT ---
            {'name': 'IF2', 'level': 0, 'base': 0.0, 'q1': 0.0, 'q2': 0.0, 'q3': 0.0, 'extra_points': 0.0},
            {'name': 'IF2', 'level': 1, 'base': 1.5, 'q1': 0.3, 'q2': 0.6, 'q3': 0.9, 'extra_points': 0.0},
            {'name': 'IF2', 'level': 2, 'base': 3.0, 'q1': 0.3, 'q2': 0.6, 'q3': 0.9, 'extra_points': 0.0},
            {'name': 'IF2', 'level': 3, 'base': 4.0, 'q1': 0.3, 'q2': 0.6, 'q3': 0.9, 'extra_points': 0.0},
            {'name': 'IF2', 'level': 4, 'base': 5.0, 'q1': 0.4, 'q2': 0.8, 'q3': 1.2, 'extra_points': 0.0},
            {'name': 'IF2', 'level': 5, 'base': 6.3, 'q1': 0.5, 'q2': 1.0, 'q3': 1.5, 'extra_points': 0.0},

            # --- SWEET TANGO ---
            {'name': 'SWT1', 'level': 0, 'base': 0.0, 'q1': 0.0, 'q2': 0.0, 'q3': 0.0, 'extra_points': 0.0},
            {'name': 'SWT1', 'level': 1, 'base': 2.0, 'q1': 0.3, 'q2': 0.6, 'q3': 0.9, 'extra_points': 0.0},
            {'name': 'SWT1', 'level': 2, 'base': 2.5, 'q1': 0.3, 'q2': 0.6, 'q3': 0.9, 'extra_points': 0.0},
            {'name': 'SWT1', 'level': 3, 'base': 3.0, 'q1': 0.3, 'q2': 0.6, 'q3': 0.9, 'extra_points': 0.0},
            {'name': 'SWT1', 'level': 4, 'base': 3.5, 'q1': 0.4, 'q2': 0.8, 'q3': 1.2, 'extra_points': 0.0},
            {'name': 'SWT1', 'level': 5, 'base': 4.5, 'q1': 0.4, 'q2': 0.8, 'q3': 1.2, 'extra_points': 0.0},
        ]

        for item in elementos_data:
            Element.objects.create(
                name=item['name'],
                level=item['level'],
                base_score=item['base'],
                qoe_1=item['q1'],
                qoe_2=item['q2'],
                qoe_3=item['q3'],
                extra_points=item['extra_points']
            )

        self.stdout.write(self.style.SUCCESS(f'Se han creado {len(elementos_data)} elementos.'))
