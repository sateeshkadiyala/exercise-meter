from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.


class Crop(models.Model):
    type = models.CharField(max_length=30)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.type


class Device(models.Model):
    row = models.PositiveIntegerField()
    column = models.PositiveIntegerField()
    serial = models.CharField(max_length=30)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_assigned = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.serial

    def get_absolute_url(self):
        return reverse('device_edit', kwargs={'pk': self.pk})


class Media(models.Model):
    name = models.CharField(max_length=20)
    value = models.DecimalField(decimal_places=2, max_digits=4)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('media_edit', kwargs={'pk': self.pk})


class Plot(models.Model):
    name = models.CharField(max_length=30)
    crop_type = models.ForeignKey(Crop, models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('plot_edit', kwargs={'pk': self.pk})


class PlotDevice(models.Model):
    plot = models.ForeignKey(Plot, on_delete=models.CASCADE)
    device = models.ForeignKey(Device, on_delete = models.CASCADE)


class PlotSetting(models.Model):
    plot = models.OneToOneField(Plot, on_delete=models.CASCADE)
    media = models.ForeignKey(Media, on_delete=models.SET_NULL, null=True)
    interval = models.PositiveIntegerField(default=1) # default interval set to a minute
    over_saturation = models.PositiveIntegerField(validators=[MaxValueValidator(100), MinValueValidator(1)])
    min_water_content = models.PositiveIntegerField(validators=[MaxValueValidator(100), MinValueValidator(1)])
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('plot_setting_edit', kwargs={'pk': self.pk})


class SensorInformation(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    water_content = models.DecimalField(decimal_places=2, max_digits=4)
    temparature = models.DecimalField(decimal_places=2, max_digits=4)
    battery_level = models.DecimalField(decimal_places=2, max_digits=4)
    created = models.DateTimeField(auto_now_add=True)


class Alert(models.Model):
    ALERT_TYPES = (
        ("frost", "Frost"),
        ("heat", "Heat"),
        ("dry", "Dry"),
        ("saturation", "Saturation"),
        ("battery", "Device Battery")
    )

    type = models.CharField(max_length=20, choices=ALERT_TYPES, default=None)
    value = models.DecimalField(decimal_places=2, max_digits=4)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.type


class GreenHouse(models.Model):
    plot = models.ForeignKey(Plot, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)