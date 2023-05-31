from rest_framework import serializers
from goal.models import Goal
from authentication.serializers import UserSerializer
from kpi.serializers import KPISerializer

class GoalSerializer(serializers.ModelSerializer):
    user = UserSerializer(many = True, read_only = True)
    kpi = KPISerializer(many = True, read_only = True)

    class Meta:
        model = Goal
        fields = ['id', 'user', 'title', 'description', 'start_date', 'end_date', 'type', 'kpi']