from rest_framework import serializers
from kpi.models import KPI

class KPISerializer(serializers.ModelSerializer):

    class Meta:
        model = KPI
        fields = ['id', 'title', 'calories', 'type', 'amount']