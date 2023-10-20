from django.urls import path, include
from rest_framework.routers import DefaultRouter

from tasks import views

router = DefaultRouter()
router.register(prefix='tasks', viewset=views.TaskViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
