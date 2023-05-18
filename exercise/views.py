from rest_framework.permissions import BasePermission
from rest_framework.viewsets import ModelViewSet
from exercise.models import Exercise
from exercise.serializers import ExerciseSerializer

class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in ['PUT', 'PATCH', 'DELETE']:
            return request.user.is_superuser
        return True

class  ExerciseViewset(ModelViewSet):
    queryset=Exercise.objects.all()
    serializer_class=ExerciseSerializer
    permission_classes = [IsAdminOrReadOnly]
