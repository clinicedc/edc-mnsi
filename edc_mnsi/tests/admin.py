import pdb

from django.contrib import admin

from edc_mnsi.admin import MnsiModelAdminMixin

from .models import Mnsi

pdb.set_trace()


@admin.register(Mnsi)
class MnsiModelAdmin(MnsiModelAdminMixin, admin.ModelAdmin):
    pass
