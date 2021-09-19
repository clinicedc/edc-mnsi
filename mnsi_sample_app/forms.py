from django import forms
from edc_crf.modelform_mixins import CrfModelFormMixin

from edc_mnsi.form_validator import MnsiFormValidator
from edc_mnsi.utils import get_mnsi_model_cls


class MnsiForm(CrfModelFormMixin, forms.ModelForm):

    form_validator_cls = MnsiFormValidator

    def validate_against_consent(self):
        """Pass for tests"""
        pass

    def validate_visit_tracking(self):
        """Pass for tests"""
        pass

    def validate_subject_schedule(self):
        """Pass for tests"""
        pass

    class Meta:
        model = get_mnsi_model_cls()
        fields = "__all__"
