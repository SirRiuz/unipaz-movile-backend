# Django
from rest_framework import serializers

# Models
from apps.califications.models.calification import Calification


class CalificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Calification
        fields = '__all__'