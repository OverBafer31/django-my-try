from rest_framework.permissions import BasePermission
from rest_framework.viewsets import ModelViewSet
from kpi.models import KPI
from kpi.serializers import KPISerializer

class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in ['PUT', 'PATCH', 'DELETE']:
            return request.user.is_superuser
        return True

class  KPIViewset(ModelViewSet):
    queryset=KPI.objects.all()
    serializer_class=KPISerializer
    permission_classes = [IsAdminOrReadOnly]
