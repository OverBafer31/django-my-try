from rest_framework import serializers
from workout.models import Workout
from exercise.serializers import ExerciseSerializer

class WorkoutSerializer(serializers.ModelSerializer):
    exercise = ExerciseSerializer(many = True, read_only = True)

    class Meta:
        model = Workout
        fields = ['id', 'title', 'description', 'type', 'calories', 'image', 'gender', 'exercise', 'difficulty', 'time', 'inventory']