from edc_model import models as edc_models

from edc_mnsi.model_mixins import MnsiModelMixin


class Mnsi(
    MnsiModelMixin,
    edc_models.BaseUuidModel,
):

    history = edc_models.HistoricalRecords()

    class Meta(MnsiModelMixin.Meta, edc_models.BaseUuidModel.Meta):
        pass
