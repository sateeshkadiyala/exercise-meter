from django import forms
from .models import *


class PlotSettingForm(forms.ModelForm):
    """
    PlotSetting form
    """
    device = forms.ModelMultipleChoiceField(Device.objects.filter(is_assigned=False))

    class Meta:
        model = PlotSetting

        fields = '__all__'

    def save(self, commit=True):

        """
        save a plot setting form
        :param commit:
        :return:
        """

        devices = self.cleaned_data['device']
        plot_id = self.cleaned_data['plot']

        for device in devices:
            pd = PlotDevice()
            pd.plot = plot_id
            pd.device = device
            device.is_assigned = True
            device.save()
            pd.save()

        return super(PlotSettingForm, self).save(commit=commit)

