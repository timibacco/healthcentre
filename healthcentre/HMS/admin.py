from django.contrib import admin

# Register your models here.
from .models import Patient, HealthProfile
class PatientAdmin(admin.ModelAdmin):
    list_display = ('healthcentre_No', 'first_name', 'last_name',  'matric_No', 'regStatus', 'kind', 'health_profile')
class HealthProfileAdmin(admin.ModelAdmin):

    list_display = ( 'Healthcentre_No','Registration_Status', 'Kind',)
    
    def Healthcentre_No(self, obj):
        return obj.patient.healthcentre_No
    def Registration_Status(self, obj):
        return obj.patient.regStatus 
    Registration_Status.boolean = True
    def Kind(self, obj):
        return obj.patient.kind
    


admin.site.register(Patient, PatientAdmin)
admin.site.register(HealthProfile, HealthProfileAdmin)
