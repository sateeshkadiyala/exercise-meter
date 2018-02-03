from .models import *
import random
from decimal import Decimal


def populate_data():

    plots = Plot.objects.all()

    for plot in plots:

        plot_setting = PlotSetting.objects.get(plot=plot)

        devices = PlotDevice.objects.filter(plot=plot)
        print(devices)
        for d in devices:
            device = Device.objects.get(id=d.device.id)
            sensor_information = SensorInformation()

            sensor_information.serial = device.serial

            temp = random.randint(1, 151)

            sensor_information.temp = temp

            if temp < 5 :
                type = "frost"
                create_alert(type, temp, device.serial, plot.name)
            if temp > 40 :
                type = "heat"
                create_alert(type, temp, device.serial, plot.name)

            water_content = random.randint(1, 100)

            sensor_information.water_content = water_content

            calculated_water_content = plot_setting.media.value * water_content

            if calculated_water_content < plot_setting.min_water_content:

                type = "dry"
                value = plot_setting.media.value * water_content
                create_alert(type, value, device.serial, plot.name)

            sensor_information.water_content = calculated_water_content

            if calculated_water_content > plot_setting.over_saturation:

                type = "saturation"

                value = plot_setting.media.value * water_content

                create_alert(type, value, device.serial, plot.name)

            battery_level = random.randint(1, 100)

            sensor_information.battery_level = battery_level

            if battery_level < 10:

                type = "battery"
                value = battery_level

                create_alert(type, value, device.serial, plot.name)

            sensor_information.save()


def create_alert(type, value, device_serial, plot):
    alert = Alert()
    alert.type = type
    alert.value = value
    alert.plot = plot
    alert.device = device_serial
    alert.save()


#populate_data()