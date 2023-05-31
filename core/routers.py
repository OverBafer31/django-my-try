from rest_framework.routers import DefaultRouter
from authentication.views import UserViewset
from exercise.views import ExerciseViewset
from workout.views import WorkoutViewset
from schedule.views import ScheduleViewset
from kpi.views import KPIViewset
from goal.views import GoalViewset

router=DefaultRouter()
router.register('auth', UserViewset)
router.register('exercises', ExerciseViewset)
router.register('workouts', WorkoutViewset)
router.register('schedule', ScheduleViewset)
router.register('KPIs', KPIViewset)
router.register('goals', GoalViewset)