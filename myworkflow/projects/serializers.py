from .models import *
from rest_framework import serializers


class DevelopmentStackSerializer(serializers.ModelSerializer):
    class Meta:
        model = DevelopmentStack
        fields = '__all__'


class PersonalProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalProject
        fields = '__all__'


class CurrentReadingBooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = CurrentReadingBook
        fields = '__all__'


class OrganizationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = '__all__'
