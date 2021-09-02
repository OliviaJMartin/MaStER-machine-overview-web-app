from django.urls import path
from . import views


urlpatterns = [
    path('', views.overview.as_view(), name='overview'),
    path('login/', views.loggingin.as_view(), name='login'),
    path('logout/', views.loggingout.as_view(), name='logout'),
    path('machinestatus/', views.status.as_view(), name='machineStatus'),
    path('updatestatus/', views.update.as_view(), name='updateStatus')
]
