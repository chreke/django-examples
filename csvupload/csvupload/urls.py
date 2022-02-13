from django.contrib import admin
from django.urls import path

from bulk.views import ImportView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('import/', ImportView.as_view()),
]
