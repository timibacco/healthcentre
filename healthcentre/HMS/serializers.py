from rest_framework import serializers
from HMS.models import Patient, HealthProfile


class HealthProfileSerializer(serializers.ModelSerializer):
    
    class Meta:
       model = HealthProfile
       fields = '__all__'
#class PatientSerializer(serializers.HyperlinkedModelSerializer):

 #   class Meta:
 #       model = Patient 
  #      fields = "__all__"

class PatientRecordClerkSerializer(serializers.ModelSerializer):
  
    
    class Meta:
        model = Patient
        fields = ['first_name','last_name','matric_No','healthcentre_No','sex','Age','kind','kinName','kinAddress','kin_relationship','kinMobile','regStatus']

class PatientMedClerkSerializer(serializers.ModelSerializer):
    health_profile= HealthProfileSerializer()
    class Meta:
        model = Patient
        fields = '__all__'
    
    def get_field_names(self, declared_fields, info):
        fields = super().get_field_names(declared_fields, info)
        fields.remove('health_profile')
        fields.append('health_profile')
        return fields
    #
    #

class PatientLabAttendantSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Patient
        fields = '__all__'
        

class UpdateHealthProfileSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = HealthProfile
        fields = '__all__'
        


