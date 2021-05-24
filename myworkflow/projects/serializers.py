from .models import *
from rest_framework import serializers


class DevelopmentStackSerializer(serializers.ModelSerializer):
    class Meta:
        model = DevelopmentStack
        fields = '__all__'
