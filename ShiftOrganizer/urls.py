from django.urls import path
from rest_framework import routers
from django.conf.urls import include
# from .views import signupfunk
from . import views

urlpatterns = [
    path('api/data', views.receive_data, name='receive_data'),
    path('api/getdata', views.get_schedule, name='get_schedule')
    # path('signup/', Signup.as_view(), name='signup'),
    ]