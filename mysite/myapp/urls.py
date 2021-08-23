from django.urls import path
from . import views

urlpatterns = [
    path('', views.overview, name='overview'),
    path('login', views.login, name='login'),
    path('machinestatus', views.status, name='machineStatus'),
    path('updatestatus', views.update, name='updateStatus')
]
