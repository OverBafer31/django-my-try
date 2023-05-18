from rest_framework.permissions import BasePermission
from rest_framework.viewsets import ModelViewSet
from workout.models import Workout
from workout.serializers import WorkoutSerializer

class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in ['PUT', 'PATCH', 'DELETE']:
            return request.user.is_superuser
        return True

class  WorkoutViewset(ModelViewSet):
    queryset=Workout.objects.all()
    serializer_class=WorkoutSerializer
    permission_classes = [IsAdminOrReadOnly]
