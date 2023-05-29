from rest_framework import serializers
from exercise.models import Exercise
from type.serializers import TypeSerializer

class ExerciseSerializer(serializers.ModelSerializer):
    type = TypeSerializer(many = True, read_only = True)

    class Meta:
        model = Exercise
        fields = ['id', 'title', 'media', 'type', 'time', 'amount', 'calories']