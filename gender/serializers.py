from rest_framework import serializers
from gender.models import Gender

class GenderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Gender
        fields = ['id', 'title']