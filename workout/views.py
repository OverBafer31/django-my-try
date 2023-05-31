from rest_framework.permissions import BasePermission
from rest_framework.viewsets import ModelViewSet
from workout.models import Workout
from workout.serializers import WorkoutSerializer
from rest_framework import generics

class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in ['PUT', 'PATCH', 'DELETE']:
            return request.user.is_superuser
        return True

class  WorkoutViewset(ModelViewSet):
    queryset=Workout.objects.all()
    serializer_class=WorkoutSerializer
    permission_classes = [IsAdminOrReadOnly]

class WorkoutList(generics.ListAPIView):
    serializer_class = WorkoutSerializer

    def get_queryset(self):
        user_id = self.request.query_params.get('user', None)
        if user_id is not None:
            queryset = Workout.objects.filter(schedule__user=user_id)
        else:
            queryset = Workout.objects.all()
        return queryset
