from django import forms

from edc_mnsi.form_validator import MnsiFormValidator

from .models import Mnsi


class MnsiForm(forms.ModelForm):

    form_validator_cls = MnsiFormValidator

    class Meta:
        model = Mnsi
        fields = "__all__"
