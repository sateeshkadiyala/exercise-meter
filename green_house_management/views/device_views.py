from ..models import *
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy


class DeviceList(ListView):
    """
    Device List View
    """
    queryset = Device.objects.all()
    context_object_name = 'devices'
    template_name = 'green_house_management/device/device_list.html'


class DeviceCreate(CreateView):
    """
    Add new device sensors
    """
    model = Device
    success_url = reverse_lazy('device_list')
    fields = ['row', 'column', 'serial', 'is_assigned', 'user']
    template_name = 'green_house_management/device/device_form.html'


class DeviceUpdate(UpdateView):
    """
    Update Device information
    """
    model = Device
    success_url = reverse_lazy('device_list')
    fields = ['row', 'column', 'serial', 'is_assigned', 'user']
    template_name = 'green_house_management/device/device_form.html'


class DeviceDelete(DeleteView):
    """
    Delete Device
    """
    model = Device
    success_url = reverse_lazy('device_list')
    template_name = 'green_house_management/device/device_confirm_delete.html'
