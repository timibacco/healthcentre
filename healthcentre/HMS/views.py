from django.shortcuts import render
from HMS.models import Patient, HealthProfile
# Create your views here.
from rest_framework import permissions, generics
from .serializers import (PatientRecordClerkSerializer, PatientMedClerkSerializer,PatientLabAttendantSerializer
)
from django.contrib.auth.models import User
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .permissions import IsMedClerk, IsRecordClerk, IsLabAttendant

########################################################################################################
class PatientRecordClerkView(generics.ListAPIView):

    # Returns a limited list of all patients [for Record Clerks only.] Active and Inactive Patients.
    # For more details on how accounts are activated please [see here][ref]. """

    queryset = Patient.objects.all()
    serializer_class = PatientRecordClerkSerializer
    permission_classes = [IsRecordClerk]

    def get_queryset(self):
       
        return super().get_queryset()


class PatientMedClerkView(generics.ListCreateAPIView):
   
# Returns a limited list of all patients [for Medical Clerks only.] Active and Inactive Patients. And create permissions for Med Clerks Only 
# For more details on how accounts are activated please [see here][ref]. """
    
    
    queryset = Patient.objects.all()
    permission_classes = [IsMedClerk]
        
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return PatientMedClerkSerializer
        else:
            return PatientMedClerkSerializer
   

class PatientLabAttendantView(generics.RetrieveUpdateAPIView):
    """ Lists or Updates all patients_medical_infos [ Lab Attendant only] Active and Inactive Patients
    For more details on how accounts are activated please  """

    queryset = Patient.objects.all()
    serializer_class = PatientLabAttendantSerializer
    permission_classes = [IsLabAttendant, permissions.IsAdminUser]