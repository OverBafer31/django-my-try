from rest_framework import serializers
from workout.models import Workout
from exercise.serializers import ExerciseSerializer
from type.serializers import TypeSerializer
from difficulty.serializers import DifficultySerializer
from equipment.serializers import EquipmentSerializer

class WorkoutSerializer(serializers.ModelSerializer):
    exercise = ExerciseSerializer(many = True, read_only = True)
    type = TypeSerializer(many = True, read_only = True)
    difficulty = DifficultySerializer(many = True, read_only = True)
    inventory = EquipmentSerializer(many = True, read_only = True)

    class Meta:
        model = Workout
        fields = ['id', 'title', 'description', 'type', 'calories', 'image', 'gender', 'exercise', 'difficulty', 'time', 'inventory']