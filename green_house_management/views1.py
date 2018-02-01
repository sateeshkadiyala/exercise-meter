from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import *
#from .forms import *
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.forms.models import model_to_dict
from django.urls import reverse, reverse_lazy

# Create your views here.

class MediaListView(ListView):
    queryset = Media.objects.all()
    context_object_name = 'media'
    template_name = 'green_house_management/media.html'


class DeviceListView(ListView):
    queryset = Device.objects.all()
    context_object_name = "devices"
    template_name = 'green_house_management/devices.html'

"""
def plot_detail(request, id):
   
    plot = get_object_or_404(Plot, id=id)

    plot_settings = PlotSetting.objects.get(plot__id=id)

    media = plot_settings.media

    # crop = plot.crop_type.all()

    devices = PlotDevice.objects.filter(plot__id=id)

    return render(request, 'green_house_management/plot_detail.html',
                  {'plot': plot, 'settings': plot_settings, 'crop': None, 'media': media,
                   'devices': devices})


def device_detail(request, id):

    device = get_object_or_404(Device, id=id)

    added = False

    if request.method == 'POST':

        device_form = DeviceForm(request.POST)

        if device_form.is_valid():

            new_device = device_form.save(commit=False)

            #new_device.post = device_detail()

            new_device.save()
    else:
        device_form = DeviceForm(initial=model_to_dict(device))


    return render(request, 'green_house_management/device_detail.html', {'device': device,
                                                                         'device_form': device_form})
"""