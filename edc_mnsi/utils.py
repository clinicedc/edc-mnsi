from django.apps import apps as django_apps
from django.conf import settings
from django.db import models


def get_mnsi_model_name() -> str:
    return getattr(settings, "EDC_MNSI_MODEL", "edc_mnsi.mnsi")


def get_mnsi_model_cls() -> models.Model:
    return django_apps.get_model(get_mnsi_model_name())


def get_abnormal_foot_appearance_obs_model_name() -> str:
    return getattr(
        settings,
        "EDC_MNSI_ABNORMAL_FOOT_APPEARANCE_OBSERVATIONS_MODEL",
        "edc_mnsi.abnormalfootappearanceobservations",
    )


def get_abnormal_foot_appearance_obs_model_cls() -> models.Model:
    return django_apps.get_model(get_abnormal_foot_appearance_obs_model_name())
