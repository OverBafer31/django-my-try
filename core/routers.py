from rest_framework.routers import DefaultRouter
from authentication.views import UserViewset
from exercise.views import ExerciseViewset
from workout.views import WorkoutViewset

router=DefaultRouter()
router.register('auth', UserViewset)
router.register('exercises', ExerciseViewset)
router.register('workouts', WorkoutViewset)
