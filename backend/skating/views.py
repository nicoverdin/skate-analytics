from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import (
    Sum, Avg, F, DecimalField, Count, ExpressionWrapper
)
from .models import Element, Skater, Result
from .serializers import ElementSerializer, SkaterSerializer, ResultSerializer
from django.db import IntegrityError
from rest_framework.exceptions import ValidationError


class ElementViewSet(viewsets.ModelViewSet):
    queryset = Element.objects.all()
    serializer_class = ElementSerializer
    filterset_fields = ['code', 'level', 'name']

    def perform_create(self, serializer):
        try:
            serializer.save()
        except IntegrityError:
            raise ValidationError({
                "detail": "An element with this generated code already exists. Adjust the level or name."
            })


class SkaterViewSet(viewsets.ModelViewSet):
    queryset = Skater.objects.all()
    serializer_class = SkaterSerializer

    def get_queryset(self):
        return super().get_queryset().annotate(
            total_score=Sum(
                ExpressionWrapper(
                    (F('results__element__base_score') +
                     F('results__element__extra_points')),
                    output_field=DecimalField(max_digits=12, decimal_places=1)
                ),
                default=0
            ),
            elements_count=Count('results')
        ).order_by('-total_score', 'name')

    @action(detail=True, methods=['get'])
    def average_scores(self, request, pk=None):
        """
        Devuelve la media de puntuación por cada tipo de elemento.
        Útil para el gráfico de radar.
        """
        qs = (
            Element.objects
            .filter(results__skater_id=pk)
            .values('name')
            .annotate(average=Avg(
                ExpressionWrapper(
                    F('base_score') + F('extra_points'),
                    output_field=DecimalField(max_digits=12, decimal_places=1)
                )
            ))
            .order_by('name')
        )
        data = [{'name': r['name'], 'average': r['average'] or 0} for r in qs]
        return Response(data)


class ResultViewSet(viewsets.ModelViewSet):
    queryset = Result.objects.all().select_related('element', 'skater')
    serializer_class = ResultSerializer
    filterset_fields = ['skater', 'element__code', 'is_program']
