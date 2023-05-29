from rest_framework.permissions import BasePermission
from rest_framework.viewsets import ModelViewSet
from schedule.models import Schedule
from schedule.serializers import ScheduleSerializer

class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in ['PUT', 'PATCH', 'DELETE']:
            return request.user.is_superuser
        return True

class  ScheduleViewset(ModelViewSet):
    queryset=Schedule.objects.all()
    serializer_class=ScheduleSerializer
    permission_classes = [IsAdminOrReadOnly]
