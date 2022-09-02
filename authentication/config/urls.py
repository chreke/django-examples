from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import ObtainAuthToken

from authentication import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path("accounts/", views.CreateUserView.as_view()),
    path("sessions/", ObtainAuthToken.as_view()),
    path("me/", views.MeView.as_view()),
]
