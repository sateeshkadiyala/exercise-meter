from ..models import *
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy


class MediaList(ListView):
    """
    List of all available media
    """
    queryset = Media.objects.all()
    context_object_name = 'media'
    template_name = 'green_house_management/media/media_list.html'


class MediaCreate(CreateView):
    """
    Media Creation view, any number of custom media can be added might need to bind to the user
    """
    model = Media
    success_url = reverse_lazy('media_list')
    fields = ['name', 'value']
    template_name = 'green_house_management/media/media_form.html'


class MediaUpdate(UpdateView):
    """
    Update media view
    """
    model = Media
    success_url = reverse_lazy('media_list')
    fields = ['name', 'value']
    template_name = 'green_house_management/media/media_form.html'


class MediaDelete(DeleteView):
    """
    Media delete view
    """
    model = Media
    success_url = reverse_lazy('media_list')
    template_name = 'green_house_management/media/media_confirm_delete.html'
