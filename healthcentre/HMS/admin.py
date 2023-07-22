from django.contrib import admin

# Register your models here.
from .models import Patient, HealthProfile
class PatientAdmin(admin.ModelAdmin):
    list_display = ('healthcentre_No', 'first_name', 'last_name',  'matric_No', 'regStatus', 'kind', 'health_profile')
class HealthProfileAdmin(admin.ModelAdmin):

    list_display = ( 'healthcentre_No','bloodGroup', 'genotype', 'weight','Kind')
    
    
    def Registration_Status(self, obj):
        return obj.medical_info.regStatus 
    Registration_Status.boolean = True
    def Kind(self, obj):
        return obj.medical_info.kind
    


admin.site.register(Patient, PatientAdmin)
admin.site.register(HealthProfile, HealthProfileAdmin)
