from rest_framework.routers import DefaultRouter
from authentication.views import UserViewset

router=DefaultRouter()
router.register('auth', UserViewset)


