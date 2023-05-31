from rest_framework import serializers
from exercise.models import Exercise

class ExerciseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Exercise
        fields = ['id', 'title', 'media', 'type', 'time', 'amount', 'calories']