from rest_framework import serializers
from difficulty.models import Difficulty

class DifficultySerializer(serializers.ModelSerializer):

    class Meta:
        model = Difficulty
        fields = ['id', 'title']