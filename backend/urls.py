from django.urls import include, path
from rest_framework.routers import SimpleRouter

from main.views import TaskViewSet

router = SimpleRouter()
router.register(r"tasks", TaskViewSet, basename="user_tasks")


urlpatterns = [
    path("api/v1/", include(router.urls)),
    path("api/v1/auth/", include("djoser.urls")),
    path("api/v1/auth/", include("djoser.urls.authtoken")),
]
