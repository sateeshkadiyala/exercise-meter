from ..models import *
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy


class PlotList(ListView):
    queryset = Plot.objects.all()
    context_object_name = 'plots'
    template_name = 'green_house_management/plot/plot_list.html'


class PlotCreate(CreateView):
    model = Plot
    success_url = reverse_lazy('plot_list')
    fields = ['name', 'crop_type']
    template_name = 'green_house_management/plot/plot_form.html'


class PlotUpdate(UpdateView):
    model = Plot
    success_url = reverse_lazy('plot_list')
    fields = ['name', 'crop_type']
    template_name = 'green_house_management/plot/plot_form.html'


class PlotDelete(DeleteView):
    model = Plot
    success_url = reverse_lazy('plot_list')
    template_name = 'green_house_management/plot/plot_confirm_delete.html'
