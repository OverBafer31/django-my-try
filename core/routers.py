from rest_framework.routers import DefaultRouter
from authentication.views import UserViewset
from exercise.views import ExerciseViewset
from workout.views import WorkoutViewset
from equipment.views import EquipmentViewset
from type.views import TypeViewset
from schedule.views import ScheduleViewset
from difficulty.views import DifficultyViewset
from gender.views import GenderViewset

router=DefaultRouter()
router.register('auth', UserViewset)
router.register('exercises', ExerciseViewset)
router.register('workouts', WorkoutViewset)
router.register('equipment', EquipmentViewset)
router.register('type', TypeViewset)
router.register('schedule', ScheduleViewset)
router.register('difficulty', DifficultyViewset)
router.register('gender', GenderViewset)
