from rest_framework.viewsets import ModelViewSet
from workout.models import Workout
from workout.serializers import WorkoutSerializer

class  WorkoutViewset(ModelViewSet):
    queryset=Workout.objects.all()
    serializer_class=WorkoutSerializer
