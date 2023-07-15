from django.contrib import admin

# Register your models here.
from .models import Patient, HealthProfile
class PatientAdmin(admin.ModelAdmin):
    list_display = ('HRNo', 'first_name', 'last_name',  'regNo', 'regStatus', 'kind')
class HealthProfileAdmin(admin.ModelAdmin):

    list_display = ('patient', 'MatricNo','Registration_Status', 'Kind',)
    
    def MatricNo(self, obj):
        return obj.patient.regNo
    def Registration_Status(self, obj):
        return obj.patient.regStatus 
    Registration_Status.boolean = True
    def Kind(self, obj):
        return obj.patient.kind
    


admin.site.register(Patient, PatientAdmin)
admin.site.register(HealthProfile, HealthProfileAdmin)
