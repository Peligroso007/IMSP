from django.urls import path

from inmsp.views.frontend import home_controller, login_controller
urlpatterns = [
    path('', home_controller.home, name='home'),
    path('login/', login_controller.Login, name='login'),
]