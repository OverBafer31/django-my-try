from rest_framework import serializers
from schedule.models import Schedule
from authentication.serializers import UserSerializer
from workout.serializers import WorkoutSerializer

class ScheduleSerializer(serializers.ModelSerializer):
    user = UserSerializer(many = True, read_only = True)
    workout = WorkoutSerializer(many = True, read_only = True)

    class Meta:
        model = Schedule
        fields = ['id', 'user', 'workout', 'date', 'time']