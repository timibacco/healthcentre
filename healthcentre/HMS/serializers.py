from rest_framework import serializers
from HMS.models import Patient, HealthProfile


class HealthProfileSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
       model = HealthProfile
       fields = '__all__'
#class PatientSerializer(serializers.HyperlinkedModelSerializer):

 #   class Meta:
 #       model = Patient 
  #      fields = "__all__"

class RClerkPatientSerializer(serializers.ModelSerializer):
  
    health_profile= serializers.CharField(source='medical_info.healthcentre_No')#  related_model = HealthProfileSerializer( )
    class Meta:
        model = Patient
        fields = '__all__'

class FullPatientSerializer(serializers.ModelSerializer):
    health_profile= serializers.CharField(source='medInfo.id')
    class Meta:
        model = Patient
        fields = '__all__'
    
    #
    #

class UpdatePatientSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Patient
        fields = '__all__'
        exclude = 'medInfo'

class UpdateHealthProfileSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = HealthProfile
        fields = '__all__'
        


