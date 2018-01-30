from django.urls import path

from . import views

urlpatterns = [
    path('plots', views.PlotListView.as_view(), name='plots'),
    path('devices', views.DeviceListView.as_view(), name='devices'),
    path('media', views.MediaListView.as_view(), name='media'),
]