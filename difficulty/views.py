from rest_framework.permissions import BasePermission
from rest_framework.viewsets import ModelViewSet
from difficulty.models import Difficulty
from difficulty.serializers import DifficultySerializer

class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in ['PUT', 'PATCH', 'DELETE']:
            return request.user.is_superuser
        return True

class  DifficultyViewset(ModelViewSet):
    queryset=Difficulty.objects.all()
    serializer_class=DifficultySerializer
    permission_classes = [IsAdminOrReadOnly]
