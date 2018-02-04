from ..models import *
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy


class AlertList(ListView):
    """
    List of alerts
    """
    queryset = Alert.objects.all()
    context_object_name = 'alerts'
    template_name = 'green_house_management/alerts/alerts_list.html'

