from rest_framework.viewsets import ModelViewSet
from authentication.models import User
from authentication.serializers import UserSerializer

class  UserViewset(ModelViewSet):
    queryset=User.objects.all()
    serializer_class=UserSerializer
