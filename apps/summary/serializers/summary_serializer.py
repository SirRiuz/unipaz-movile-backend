# Django
from rest_framework import serializers

# Models
from apps.summary.models.summary import Summary


class SummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Summary
        fields = '__all__'