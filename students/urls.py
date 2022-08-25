from rest_framework.routers import DefaultRouter

from students.views import StudentViewSet,ActivityViewSet

router = DefaultRouter()

router.register('students', StudentViewSet, basename='student')
router.register('activities', ActivityViewSet, basename='activity')

urlpatterns = []

urlpatterns += router.urls
