from django.urls import include, path
from rest_framework.routers import DefaultRouter

from tasks import views


router = DefaultRouter()
router.register(prefix="tasks", viewset=views.TaskViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
