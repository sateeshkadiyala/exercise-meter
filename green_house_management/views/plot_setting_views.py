from ..models import Device, PlotDevice, PlotSetting
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from django.shortcuts import render, get_object_or_404
from ..forms import PlotSettingForm
from django.http import Http404, HttpResponse
import logging, sys
from django.core.exceptions import EmptyResultSet, ObjectDoesNotExist, ValidationError
from django.db import DatabaseError


logger = logging.getLogger(__name__)


def plot_setting_list(request):
    """
    :param request:
    :return: a list view of plot_settings
    """

    try:
        settings = PlotSetting.objects.all()
    except EmptyResultSet:
        logger.info(sys.exc_info())

    devices = PlotDevice.objects.filter()

    return render(request, 'green_house_management/plot_setting/plot_setting_list.html',
                  {'settings': settings, 'devices': devices})


def plot_setting_new(request):
    """
    :param request:
    :return: a list view to create plot_setting
    """

    setting = PlotSetting()

    setting_form = PlotSettingForm(request.POST)

    if setting_form.is_valid():

        try:

            setting = setting_form.save()

            setting.save()

        except Exception:
            logger.error(sys.exc_info())

    return render(request, 'green_house_management/plot_setting/plot_setting_form.html', {'setting': setting, 'setting_form': setting_form})


def plot_setting_edit(request, pk):
    """

    :param request:
    :param pk:
    :return: Edit a new plot setting
    """
    try:
        setting = PlotSetting.objects.get(id=pk)
        if request.method == 'POST':

            setting_form = PlotSettingForm(instance=setting)

            request_data = dict(request.POST)

            device_list = request_data['device']

            devices = []

            if setting_form.is_valid():

                for d in device_list:
                    devices.append(Device.objects.get(id=d))

                # save devices

                for device in devices:
                    pd = PlotDevice()
                    pd.plot = setting.plot
                    pd.device = device
                    device.is_assigned = True
                    device.save()
                    pd.save()

                new_setting = setting_form.save(commit=False)

                new_setting.save()
        else:
            setting_form = PlotSettingForm(instance=setting)

    except ObjectDoesNotExist:
        logger.error(sys.exc_info())

    except DatabaseError:
        logger.error(sys.exc_info())

    return render(request, 'green_house_management/plot_setting/plot_setting_form.html', {'setting': setting, 'setting_form': setting_form})


class PlotSettingDelete(DeleteView):
    """
    A Plot Setting Delete view class which retrieves a specified object and delte it.
    """
    def get_object(self, queryset=None):
        try:

            plotSetting = super(PlotSettingDelete, self).get_object()

            plot_devices = PlotDevice.objects.filter(plot=plotSetting.plot)

            for plot_device in plot_devices:
                device = Device.objects.get(id=plot_device.device.id)
                device.is_assigned = False
                print(device)
                device.save()

        except ObjectDoesNotExist:
            logger.error(sys.exc_info())

        return plotSetting

    model = PlotSetting

    success_url = reverse_lazy('plot_setting_list')

    template_name = 'green_house_management/plot_setting/plot_setting_confirm_delete.html'


