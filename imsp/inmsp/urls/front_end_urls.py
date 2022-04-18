from django.urls import path

from inmsp.views.frontend import home_controller
urlpatterns = [
    path('', home_controller.home, name='home'),
]