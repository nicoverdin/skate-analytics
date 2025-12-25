from rest_framework import serializers
from .models import Element, Skater, Result
from django.contrib.auth.models import User


class ElementSerializer(serializers.ModelSerializer):
    total_score = serializers.SerializerMethodField()

    class Meta:
        model = Element
        fields = ['id', 'code', 'name', 'level', 'base_score', 'extra_points',
                  'total_score']
        read_only_fields = ['code']

    def get_total_score(self, obj):
        return float(obj.base_score + obj.extra_points)


class SkaterSerializer(serializers.ModelSerializer):
    username = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)

    total_score = serializers.DecimalField(
        max_digits=12, decimal_places=1, read_only=True
    )

    elements_count = serializers.IntegerField(read_only=True)

    free_elements = serializers.ListField(
        child=serializers.CharField(max_length=20),
        allow_empty=True,
        required=False
    )

    style_elements = serializers.ListField(
        child=serializers.CharField(max_length=20),
        allow_empty=True,
        required=False
    )

    class Meta:
        model = Skater
        fields = ['id', 'name', 'total_score', 'elements_count',
                  'free_elements', 'style_elements', 'username',
                  'password']

    def create(self, validated_data):
        username = validated_data.pop('username')
        password = validated_data.pop('password')

        user = User.objects.create_user(username=username, password=password)

        skater = Skater.objects.create(user=user, **validated_data)
        return skater


class ResultSerializer(serializers.ModelSerializer):
    element_details = ElementSerializer(source='element', read_only=True)
    total_score = serializers.ReadOnlyField()

    class Meta:
        model = Result
        fields = ['id', 'skater', 'element', 'element_details', 'qoe_given',
                  'total_score', 'date', 'notes', 'is_program']


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'is_staff')
