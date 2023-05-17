from rest_framework import serializers
from exercise.models import Exercise

class ExerciseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Exercise
        fields = ['id', 'title', 'hardness', 'amount', 'media', 'show_timer', 'calories', 'equipment']