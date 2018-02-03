from ..models import *
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from django.shortcuts import render, get_object_or_404
from ..forms import *
from django.forms.models import model_to_dict
import json
from django.http import Http404, HttpResponse


def plot_setting_list(request):

    settings = PlotSetting.objects.all()

    devices = PlotDevice.objects.filter()

    return render(request, 'green_house_management/plot_setting/plot_setting_list.html',
                  {'settings': settings, 'devices': devices})


def plot_setting_new(request):

    setting = PlotSetting()

    setting_form = PlotSettingForm(request.POST)

    print(request.POST)

    if setting_form.is_valid():

        setting = setting_form.save()

        setting.save()
    return render(request, 'green_house_management/plot_setting/plot_setting_form.html', {'setting': setting, 'setting_form': setting_form})


def plot_setting_edit(request, pk):
    setting = PlotSetting.objects.get(id=pk)

    if request.method == 'POST':

        setting_form = PlotSettingForm(instance=setting)

        myDict = dict(request.POST)

        print(myDict['device'])

        device = Device.objects.get(id=myDict['device'][0])

        pd = PlotDevice()
        pd.plot = setting.plot
        pd.device = device
        device.is_assigned = True
        device.save()
        pd.save()

        if setting_form.is_valid():
            new_device = setting_form.save(commit=False)

            new_device.save()
    else:
        setting_form = PlotSettingForm(instance=setting)
    return render(request, 'green_house_management/plot_setting/plot_setting_form.html', {'setting': setting, 'setting_form': setting_form})

def PlotSettingList(ListView):
    queryset = PlotSetting.objects.all()
    context_object_name = 'plot_settings'
    template_name = 'green_house_management/plot_setting/plot_setting_list.html'


class PlotSettingCreate(CreateView):
    model = PlotSetting
    success_url = reverse_lazy('plot_setting_list')
    fields = ['plot', 'media', 'interval', 'over_saturation', 'min_water_content', 'user']
    template_name = 'green_house_management/plot_setting/plot_setting_form.html'


class PlotSettingUpdate(UpdateView):
    model = PlotSetting
    success_url = reverse_lazy('plot_setting_list')
    fields = ['plot', 'media', 'interval', 'over_saturation', 'min_water_content', 'user']
    template_name = 'green_house_management/plot_setting/plot_setting_form.html'


class PlotSettingDelete(DeleteView):
    def get_object(self, queryset=None):
        """ Hook to ensure object is owned by request.user. """
        plotSetting = super(PlotSettingDelete, self).get_object()
        plot_devices = PlotDevice.objects.filter(plot=plotSetting.plot)
        print(plot_devices)
        for plot_device in plot_devices:
            device = Device.objects.get(id=plot_device.device.id)
            device.is_assigned = False
            print(device)
            device.save()
        if not plotSetting.user == self.request.user:
            raise Http404
        return plotSetting
    model = PlotSetting
    success_url = reverse_lazy('plot_setting_list')
    template_name = 'green_house_management/plot_setting/plot_setting_confirm_delete.html'


