from rest_framework import serializers

from learning.models import CurrentReadingBook


class CurrentReadingBooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = CurrentReadingBook
        fields = '__all__'
