from rest_framework.permissions import BasePermission
from rest_framework.viewsets import ModelViewSet
from gender.models import Gender
from gender.serializers import GenderSerializer

class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in ['PUT', 'PATCH', 'DELETE']:
            return request.user.is_superuser
        return True

class  GenderViewset(ModelViewSet):
    queryset=Gender.objects.all()
    serializer_class=GenderSerializer
    permission_classes = [IsAdminOrReadOnly]
