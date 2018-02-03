from django import forms
from .models import *


class PlotSettingForm(forms.ModelForm):
    device = forms.ModelMultipleChoiceField(Device.objects.filter(is_assigned=False))

    class Meta:
        model = PlotSetting

        fields = '__all__'

    def save(self, commit=True):

        devices = self.cleaned_data['device']
        plot_id = self.cleaned_data['plot']

        print("printing in the save of the form...")

        for device in devices:
            pd = PlotDevice()
            pd.plot = plot_id
            pd.device = device
            device.is_assigned = True
            device.save()
            pd.save()

        return super(PlotSettingForm, self).save(commit=commit)

