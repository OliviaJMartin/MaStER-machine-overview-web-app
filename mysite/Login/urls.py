from django.urls import path
from . import views
# from .views import redirect_overview, redirect_machinestatus


urlpatterns = [
    path('', views.index, name='index'),
    # path('redirectOverview/', redirect_overview),
    # path('redirectMachineStatus/', redirect_machinestatus)
]