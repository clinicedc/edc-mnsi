from django.db.models.signals import post_save
from django.dispatch import receiver
from edc_list_data.model_mixins import ListModelMixin


class AbnormalFootAppearanceObservations(ListModelMixin):
    class Meta(ListModelMixin.Meta):
        verbose_name = "Abnormal Foot Appearance Observations"
        verbose_name_plural = "Abnormal Foot Appearance Observations"


@receiver(post_save, weak=False, dispatch_uid="calculate_mnsi_score_on_post_save")
def calculate_mnsi_score_on_post_save(sender, instance, raw, created, using, **kwargs):
    if not raw and not kwargs.get("update_fields"):
        try:
            instance.update_mnsi_calculated_fields()
        except AttributeError as e:
            if "update_mnsi_calculated_fields" not in str(e):
                raise
