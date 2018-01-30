from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import *
from django.views.generic import ListView

# Create your views here.


class PlotListView(ListView):
    queryset = Plot.objects.all()
    context_object_name = 'plots'
    template_name = 'green_house_management/plots.html'


class MediaListView(ListView):
    queryset = Media.objects.all()
    context_object_name = 'media'
    template_name = 'green_house_management/media.html'


class DeviceListView(ListView):
    queryset = Device.objects.all()
    context_object_name = "devices"
    template_name = 'green_house_management/devices.html'