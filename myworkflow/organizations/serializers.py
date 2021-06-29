from .models import *
from rest_framework import serializers


class OrganizationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = '__all__'
