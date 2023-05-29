from rest_framework.permissions import BasePermission
from rest_framework.viewsets import ModelViewSet
from type.models import Type
from type.serializers import TypeSerializer

class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in ['PUT', 'PATCH', 'DELETE']:
            return request.user.is_superuser
        return True

class  TypeViewset(ModelViewSet):
    queryset=Type.objects.all()
    serializer_class=TypeSerializer
    permission_classes = [IsAdminOrReadOnly]
