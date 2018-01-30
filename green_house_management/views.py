from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import *

# Create your views here.


def plots_list(request):

    plots = Plot.objects.all()
    t = loader.get_template('green_house_management/plots.html')
    c = {'plots' : plots}
    return HttpResponse(t.render(c, request))


def media_list(request):

    media = Media.objects.all()
    t = loader.get_template('green_house_management/media.html')
    c = {'media' : media}
    return HttpResponse(t.render(c, request))


def devices_list(request):

    devices = Device.objects.all()
    t = loader.get_template('green_house_management/devices.html')
    c = {'devices' : devices}
    return HttpResponse(t.render(c, request))