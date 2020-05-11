from django.contrib import admin
from .models import Hospital
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class HospitalResource(resources.ModelResource):
    class Meta:
        model = Hospital

class HospitalAdmin(ImportExportModelAdmin):
    resource_class = HospitalResource

# Register your models here.
admin.site.register(Hospital, HospitalAdmin)

