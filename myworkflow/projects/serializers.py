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


class UniversityProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UniversityProject
        fields = '__all__'


class UniversityClassesSerializer(serializers.ModelSerializer):
    class Meta:
        model = UniversityClasses
        fields = '__all__'
