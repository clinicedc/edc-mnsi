from django.contrib import admin
from django_audit_fields import audit_fieldset_tuple
from edc_crf.admin import CrfStatusModelAdminMixin, crf_status_fieldset_tuple
from edc_form_label.form_label_modeladmin_mixin import FormLabelModelAdminMixin
from edc_model_admin import SimpleHistoryAdmin
from edc_model_admin.dashboard import ModelAdminCrfDashboardMixin

from edc_mnsi.admin_site import edc_mnsi_admin
from edc_mnsi.fieldsets import calculated_values_fieldset
from edc_mnsi.fieldsets import get_fieldsets as get_mnsi_fieldsets
from edc_mnsi.model_admin_mixin import MnsiModelAdminMixin
from edc_mnsi.utils import get_mnsi_model_cls

from .forms import MnsiForm


def get_fieldsets():
    fieldset = (
        None,
        {
            "fields": (
                "subject_visit",
                "report_datetime",
                "mnsi_performed",
                "mnsi_not_performed_reason",
            )
        },
    )

    fieldsets = (fieldset,) + get_mnsi_fieldsets()
    fieldsets += (crf_status_fieldset_tuple,)
    fieldsets += (calculated_values_fieldset,)
    fieldsets += (audit_fieldset_tuple,)
    return fieldsets


@admin.register(get_mnsi_model_cls(), site=edc_mnsi_admin)
class MnsiAdmin(
    MnsiModelAdminMixin,
    ModelAdminCrfDashboardMixin,
    FormLabelModelAdminMixin,
    CrfStatusModelAdminMixin,
    SimpleHistoryAdmin,
):

    form = MnsiForm

    fieldsets = get_fieldsets()
