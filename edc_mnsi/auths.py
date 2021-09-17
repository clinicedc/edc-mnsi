from edc_auth.site_auths import site_auths

from .auth_objects import MNSI, MNSI_EXPORT, MNSI_SUPER, MNSI_VIEW

site_auths.add_group(
    "edc_mnsi.view_mnsi",
    # "edc_mnsi.view_historicalmnsi",
    name=MNSI_VIEW,
)

site_auths.add_group(
    "edc_mnsi.add_mnsi",
    "edc_mnsi.change_mnsi",
    "edc_mnsi.view_mnsi",
    # "edc_mnsi.view_historicalmnsi",
    name=MNSI,
)

site_auths.add_group(
    "edc_mnsi.delete_mnsi",
    "edc_mnsi.add_mnsi",
    "edc_mnsi.change_mnsi",
    "edc_mnsi.view_mnsi",
    # "edc_mnsi.view_historicalmnsi",
    name=MNSI_SUPER,
)

site_auths.add_group(
    "edc_mnsi.export_mnsi",
    name=MNSI_EXPORT,
)
