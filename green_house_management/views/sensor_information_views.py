from ..generate_data import *
from django.http import Http404, HttpResponse
from django.shortcuts import render, get_object_or_404
from bson import json_util


def sensor_information(request):

    """
    Generate new sensor information

    :param request:
    :return:
    """

    download_sensor_data()

    return render(request, 'green_house_management/sensor_information.html')