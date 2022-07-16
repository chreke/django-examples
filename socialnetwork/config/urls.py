from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter

from socialnetwork.views import UserViewSet

router = DefaultRouter()
router.register("users", UserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
] + router.urls
