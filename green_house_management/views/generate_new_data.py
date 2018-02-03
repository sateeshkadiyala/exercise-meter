from ..generate_data import *
from django.http import Http404, HttpResponse
from django.shortcuts import render, get_object_or_404


def generate_new_data(request):

    populate_data()

    return render(request, 'green_house_management/data.html')