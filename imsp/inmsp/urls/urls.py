from django.urls import path
from inmsp.views import admin_controller


urlpatterns = [
    path('admin/dashboard/', admin_controller.dashboard, name='admin'),
]