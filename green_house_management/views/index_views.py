from ..generate_data import *
from django.http import Http404, HttpResponse
from django.shortcuts import render, get_object_or_404


def index(request):

    """
    Landing view
    :param request:
    :return:
    """

    return render(request, 'green_house_management/index.html')