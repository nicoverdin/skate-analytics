from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import (
    Sum, F, DecimalField, Count, ExpressionWrapper
)
from .models import Element, Skater, Result
from .serializers import ElementSerializer, SkaterSerializer, ResultSerializer
from django.db import IntegrityError
from rest_framework.exceptions import ValidationError
from collections import defaultdict


class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        # Si la petición es de lectura (GET, HEAD, OPTIONS)
        if request.method in permissions.SAFE_METHODS:
            return request.user and request.user.is_authenticated

        # Para crear (POST), editar o borrar, debe ser staff
        return request.user and request.user.is_staff


class ElementViewSet(viewsets.ModelViewSet):
    queryset = Element.objects.all()
    serializer_class = ElementSerializer
    filterset_fields = ['code', 'level', 'name']
    permission_classes = [IsAdminOrReadOnly]

    def perform_create(self, serializer):
        try:
            serializer.save()
        except IntegrityError:
            raise ValidationError({
                "detail": "An element with this generated code already exists."
            })


class SkaterViewSet(viewsets.ModelViewSet):
    serializer_class = SkaterSerializer
    permission_classes = [IsAdminOrReadOnly]

    def get_queryset(self):
        queryset = Skater.objects.annotate(
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

        user = self.request.user
        if not user.is_staff:
            queryset = queryset.filter(user=user)

        return queryset

    @action(detail=True, methods=['get'])
    def stats(self, request, pk=None):
        skater = self.get_object()
        results = Result.objects.filter(skater=skater).select_related('element')

        grouped_data = defaultdict(list)
        for res in results:
            grouped_data[res.element.name].append(res.total_score)

        stats = []
        for element_name, scores in grouped_data.items():
            stats.append({
                'element__name': element_name,
                'average': sum(scores) / len(scores) if scores else 0
            })

        return Response(stats)

    def perform_create(self, serializer):
        if not self.request.user.is_staff:
            serializer.save(user=self.request.user)
        else:
            serializer.save()


class ResultViewSet(viewsets.ModelViewSet):
    serializer_class = ResultSerializer
    filterset_fields = ['skater', 'element__code', 'is_program']

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Result.objects.all().order_by('-date')

        return Result.objects.filter(
            skater__user=user
        ).order_by('-date')
