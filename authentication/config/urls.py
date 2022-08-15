from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import ObtainAuthToken

from authentication import views

router = DefaultRouter()

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", views.CreateUserView.as_view()),
    path("sessions/", ObtainAuthToken.as_view()),
    path("me/", views.MeView.as_view()),
]
