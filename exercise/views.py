from rest_framework.viewsets import ModelViewSet
from exercise.models import Exercise
from exercise.serializers import ExerciseSerializer

class  ExerciseViewset(ModelViewSet):
    queryset=Exercise.objects.all()
    serializer_class=ExerciseSerializer
