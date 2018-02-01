from ..models import *
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy


class MediaList(ListView):
    queryset = Media.objects.all()
    context_object_name = 'media'
    template_name = 'green_house_management/media/media_list.html'


class MediaCreate(CreateView):
    model = Media
    success_url = reverse_lazy('media_list')
    fields = ['name', 'value']
    template_name = 'green_house_management/media/media_form.html'


class MediaUpdate(UpdateView):
    model = Media
    success_url = reverse_lazy('media_list')
    fields = ['name', 'value']
    template_name = 'green_house_management/media/media_form.html'


class MediaDelete(DeleteView):
    model = Media
    success_url = reverse_lazy('media_list')
    template_name = 'green_house_management/media/media_confirm_delete.html'
