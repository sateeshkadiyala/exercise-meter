from ..models import *
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy


class PlotSettingList(ListView):
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
    model = PlotSetting
    success_url = reverse_lazy('plot_setting_list')
    template_name = 'green_house_management/plot_setting/plot_setting_confirm_delete.html'
