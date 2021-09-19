from django.conf import settings
from django.db import models
from edc_crf.crf_model_mixin import CrfModelMixin
from edc_crf.crf_status_model_mixin import CrfStatusModelMixin
from edc_identifier.model_mixins import NonUniqueSubjectIdentifierFieldMixin
from edc_model import models as edc_models
from edc_model.models import BaseUuidModel
from edc_utils import get_utcnow
from edc_visit_schedule.model_mixins import VisitCodeFieldsModelMixin

from edc_mnsi.model_mixins import MnsiModelMixin


class Appointment(
    NonUniqueSubjectIdentifierFieldMixin, VisitCodeFieldsModelMixin, BaseUuidModel
):
    class Meta(BaseUuidModel.Meta):
        pass


class SubjectVisit(
    NonUniqueSubjectIdentifierFieldMixin, VisitCodeFieldsModelMixin, BaseUuidModel
):

    appointment = models.ForeignKey(Appointment, on_delete=models.PROTECT, related_name="+")

    report_datetime = models.DateTimeField(default=get_utcnow)

    class Meta(BaseUuidModel.Meta):
        pass


class Mnsi(
    MnsiModelMixin,
    CrfModelMixin,
    CrfStatusModelMixin,
    edc_models.BaseUuidModel,
):
    subject_visit = models.OneToOneField(
        settings.SUBJECT_VISIT_MODEL, on_delete=models.PROTECT
    )

    def update_crf_status_for_instance(self):
        """Pass for tests"""
        pass

    def validate_subject_schedule_status(self):
        """Pass for tests"""
        pass

    def validate_visit_sequence(self):
        """Pass for tests"""
        pass

    def validate_study_status(self):
        """Pass for tests"""
        pass

    class Meta(MnsiModelMixin.Meta, edc_models.BaseUuidModel.Meta):
        pass
