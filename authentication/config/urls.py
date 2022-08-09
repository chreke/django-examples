from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter

from authentication import views

router = DefaultRouter()

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", views.CreateAccountView.as_view()),
]
