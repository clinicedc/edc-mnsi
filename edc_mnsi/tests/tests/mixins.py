from django.apps import apps as django_apps
from django.test import TestCase
from edc_constants.constants import (
    ABSENT,
    NO,
    NORMAL,
    NOT_APPLICABLE,
    NOT_EXAMINED,
    OTHER,
    PRESENT,
    YES,
)
from edc_list_data import site_list_data

from edc_mnsi import list_data
from edc_mnsi.model_mixins import abnormal_foot_appearance_observations_model

from ..models import Mnsi


class TestCaseMixin(TestCase):

    foot_choices = ["right", "left"]

    @classmethod
    def setUpTestData(cls):
        site_list_data.initialize()
        site_list_data.register(list_data, app_name="edc_mnsi")
        site_list_data.load_data()

    @staticmethod
    def get_mnsi_obj(abnormal_obs_left_foot=None, abnormal_obs_right_foot=None, **responses):
        """Returns an Mnsi model instance with the m2ms added"""
        mnsi = Mnsi(**responses)
        mnsi.save()
        for obj in abnormal_obs_left_foot:
            mnsi.abnormal_obs_left_foot.add(obj)
        for obj in abnormal_obs_right_foot:
            mnsi.abnormal_obs_right_foot.add(obj)
        return mnsi

    @staticmethod
    def get_empty_abnormal_obs_set():
        return django_apps.get_model(
            abnormal_foot_appearance_observations_model
        ).objects.filter(name=None)

    @staticmethod
    def get_nonempty_abnormal_obs_set(value="infection"):
        return django_apps.get_model(
            abnormal_foot_appearance_observations_model
        ).objects.filter(name=value)

    @property
    def amputated_abnormal_obs_sets(self):
        return [
            self.get_nonempty_abnormal_obs_set("deformity_amputation"),
            self.get_amputation_plus_other_abnormalities_set(),
        ]

    @staticmethod
    def get_amputation_plus_other_abnormalities_set():
        return django_apps.get_model(
            abnormal_foot_appearance_observations_model
        ).objects.exclude(name__contains=OTHER)

    def get_best_case_answers(self):
        data = {
            "mnsi_performed": YES,
            "mnsi_not_performed_reason": None,
        }
        data.update(self.get_best_case_patient_history_data())
        data.update(self.get_best_case_physical_assessment_data())
        return data

    @staticmethod
    def get_best_case_patient_history_data():
        return {
            # Part 1: Patient History
            "numb_legs_feet": NO,
            "burning_pain_legs_feet": NO,
            "feet_sensitive_touch": NO,
            "muscle_cramps_legs_feet": NO,  # no effect on score, regardless of value
            "prickling_feelings_legs_feet": NO,
            "covers_touch_skin_painful": NO,
            "differentiate_hot_cold_water": YES,
            "open_sore_foot_history": NO,
            "diabetic_neuropathy": NO,
            "feel_weak": NO,  # no effect on score, regardless of value
            "symptoms_worse_night": NO,
            "legs_hurt_when_walk": NO,
            "sense_feet_when_walk": YES,
            "skin_cracks_open_feet": NO,
            "amputation": NO,
        }

    def get_best_case_physical_assessment_data(self):
        data = {}
        for foot_choice in self.foot_choices:
            data.update(
                {
                    f"normal_appearance_{foot_choice}_foot": YES,
                    f"abnormal_obs_{foot_choice}_foot": self.get_empty_abnormal_obs_set(),
                    f"ulceration_{foot_choice}_foot": ABSENT,
                    f"ankle_reflexes_{foot_choice}_foot": PRESENT,
                    f"vibration_perception_{foot_choice}_toe": PRESENT,
                    f"monofilament_{foot_choice}_foot": NORMAL,
                }
            )
        return data

    def get_mnsi_not_performed_answers(self):
        data = {
            "mnsi_performed": NO,
            "mnsi_not_performed_reason": "e.g. right foot in bandage",
            # Part 1: Patient History
            "numb_legs_feet": NOT_APPLICABLE,
            "burning_pain_legs_feet": NOT_APPLICABLE,
            "feet_sensitive_touch": NOT_APPLICABLE,
            "muscle_cramps_legs_feet": NOT_APPLICABLE,
            "prickling_feelings_legs_feet": NOT_APPLICABLE,
            "covers_touch_skin_painful": NOT_APPLICABLE,
            "differentiate_hot_cold_water": NOT_APPLICABLE,
            "open_sore_foot_history": NOT_APPLICABLE,
            "diabetic_neuropathy": NOT_APPLICABLE,
            "feel_weak": NOT_APPLICABLE,
            "symptoms_worse_night": NOT_APPLICABLE,
            "legs_hurt_when_walk": NOT_APPLICABLE,
            "sense_feet_when_walk": NOT_APPLICABLE,
            "skin_cracks_open_feet": NOT_APPLICABLE,
            "amputation": NOT_APPLICABLE,
        }
        for foot_choice in self.foot_choices:
            data.update(
                {
                    f"normal_appearance_{foot_choice}_foot": NOT_EXAMINED,
                    f"abnormal_obs_{foot_choice}_foot": self.get_empty_abnormal_obs_set(),
                    f"ulceration_{foot_choice}_foot": NOT_EXAMINED,
                    f"ankle_reflexes_{foot_choice}_foot": NOT_EXAMINED,
                    f"vibration_perception_{foot_choice}_toe": NOT_EXAMINED,
                    f"monofilament_{foot_choice}_foot": NOT_EXAMINED,
                }
            )
        return data

    @staticmethod
    def get_worst_case_patient_history_data():
        return {
            # Part 1: Patient History
            "numb_legs_feet": YES,
            "burning_pain_legs_feet": YES,
            "feet_sensitive_touch": YES,
            "prickling_feelings_legs_feet": YES,
            "covers_touch_skin_painful": YES,
            "differentiate_hot_cold_water": NO,
            "open_sore_foot_history": YES,
            "diabetic_neuropathy": YES,
            "symptoms_worse_night": YES,
            "legs_hurt_when_walk": YES,
            "sense_feet_when_walk": NO,
            "skin_cracks_open_feet": YES,
            "amputation": YES,
        }

    def get_worst_case_physical_assessment_data(self):
        data = {}
        for foot_choice in self.foot_choices:
            data.update(
                {
                    f"normal_appearance_{foot_choice}_foot": NO,
                    f"abnormal_obs_{foot_choice}_foot": self.get_nonempty_abnormal_obs_set(),
                    f"ulceration_{foot_choice}_foot": PRESENT,
                    f"ankle_reflexes_{foot_choice}_foot": ABSENT,
                    f"vibration_perception_{foot_choice}_toe": ABSENT,
                    f"monofilament_{foot_choice}_foot": ABSENT,
                }
            )
        return data
