from django.urls import path

from . import views

urlpatterns = [
    path('plots', views.plots_list, name='plots'),
    path('devices', views.devices_list, name='devices'),
    path('media', views.media_list, name='media'),
]