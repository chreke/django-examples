from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter

from socialnetwork.views import UserViewSet, FollowersListView

router = DefaultRouter()
router.register("users", UserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path(
        "users/<slug:username>/followers/",
        FollowersListView.as_view(),
        name="user-followers",
    )
] + router.urls
