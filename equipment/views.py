from rest_framework.permissions import BasePermission
from rest_framework.viewsets import ModelViewSet
from equipment.models import Equipment
from equipment.serializers import EquipmentSerializer

class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in ['PUT', 'PATCH', 'DELETE']:
            return request.user.is_superuser
        return True

class  EquipmentViewset(ModelViewSet):
    queryset=Equipment.objects.all()
    serializer_class=EquipmentSerializer
    permission_classes = [IsAdminOrReadOnly]
