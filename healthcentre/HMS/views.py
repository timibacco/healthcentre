from django.shortcuts import render
from HMS.models import Patient, HealthProfile
# Create your views here.
from rest_framework import permissions, generics
from .serializers import (PatientRecordClerkSerializer, PatientMedClerkSerializer,PatientLaboratoristSerializer
)
from django.contrib.auth.models import User
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .permissions import IsMedClerk, IsRecordClerk, IsLabAttendant
from django.shortcuts import get_object_or_404
########################################################################################################
class PatientRecordClerkView(generics.ListAPIView):

    # Returns a limited list of all patients [for Record Clerks only.] Active and Inactive Patients.
    # For more details on how accounts are activated please [see here][ref]. """

    queryset = Patient.objects.all()
    serializer_class = PatientRecordClerkSerializer
    permission_classes = []

    def get_queryset(self):
        
        return super().get_queryset()

#class MultipleFieldLookupMixin:



    """ def get_object(self):
        queryset = self.get_queryset()             # Get the base queryset
        queryset = self.filter_queryset(queryset)  # Apply any filter backends
        filter = {}
        for field in self.lookup_fields:
            if self.kwargs.get(field): # Ignore empty fields.
                filter[field] = self.kwargs[field]
        obj = get_object_or_404(queryset, **filter)  # Lookup the object
        self.check_object_permissions(self.request, obj)
        return obj     """

#class RetrieveRecordClerkView(MultipleFieldLookupMixin, generics.RetrieveAPIView):
    """ Retrieving patients using other fields other than {{id}}. More Like a Search endpoint is what it is.
     
    queryset = Patient.objects.all()
    serializer_class = PatientRecordClerkView
    lookup_fields = ['matric_No','healthcentre_No']
    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False):
            return Patient.objects.none()  # return empty queryset
        return Patient.get_object()"""

#################################################################################################################
#################################################################################################################


class PatientMedClerkView(generics.ListCreateAPIView):
   
# Returns a limited list of all patients [for Medical Clerks only.] Active and Inactive Patients. And create permissions for Med Clerks Only 
# For more details please see [Author] """
    
    
    queryset = Patient.objects.all()
   # permission_classes = [IsMedClerk]
        
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return PatientMedClerkSerializer
        else:
            return PatientMedClerkSerializer
   

class PatientLaboratoristView(generics.RetrieveUpdateDestroyAPIView):
    """ Lists or Updates all patients_medical_infos [ Lab Attendant only] .Active and Inactive Patients
    For more details on how accounts are activated please see [ Author ]  """

    queryset = Patient.objects.all()
    serializer_class = PatientLaboratoristSerializer
   # permission_classes = [IsLabAttendant, permissions.IsAdminUser]


class LoginAPIView(GenericAPIView):
    def post(self, request):
        username = request.POST('username')
        password = request.POST('password')
        user = authenticate(username=username, password=password)