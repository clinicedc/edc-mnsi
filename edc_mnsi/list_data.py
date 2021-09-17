from edc_constants.constants import OTHER

from .utils import get_abnormal_foot_appearance_obs_model_name

list_data = {
    get_abnormal_foot_appearance_obs_model_name(): [
        ("callous_formation", "Callous formation"),
        ("deformity_amputation", "Deformity – amputation"),
        ("deformity_flat_feet", "Deformity – flat feet"),
        ("deformity_halux_valgus", "Deformity – halux valgus"),
        ("deformity_hammer_toes", "Deformity – hammer toes"),
        ("deformity_joint_subluxation", "Deformity – joint subluxation"),
        ("deformity_medial_convexity", "Deformity – medial convexity (Charcot foot)"),
        ("deformity_overlapping_toes", "Deformity – overlapping toes"),
        ("deformity_prominent_metatarsal_heads", "Deformity – prominent metatarsal heads"),
        ("dry_skin", "Dry skin"),
        ("infection", "Infection"),
        ("fissure", "Fissure"),
        (OTHER, "Other abnormality, please specify"),
    ],
}
