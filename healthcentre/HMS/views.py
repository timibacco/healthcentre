from django.shortcuts import render
from HMS.models import Patient, HealthProfile
# Create your views here.
from rest_framework import permissions
from .serializers import (RClerkPatientSerializer, FullPatientSerializer, 
 UpdateHealthProfileSerializer,UpdatePatientSerializer
)
from django.contrib.auth.models import User
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class PatientListView(APIView):


    """ Returns list of all patients. Active and Inactive.
     For more details on how accounts are activated please [see here][ref]. """

    permission_classes = [permissions.IsAuthenticated]
    
    def get_serializer_class(self):    # Get serializer class
        user = self.request.user   
        user = User.objects.get(username=user)       # Get user's object and 
        if self.request.method == 'GET':
            if user.groups.filter(name='record clerk').exists():        # it's group passed a condition to view
                return RClerkPatientSerializer      # just a few fields we've defined in it's serializer
            return FullPatientSerializer
        elif self.request.method == 'POST':
            if user.groups.filter(name='medical clerk').exists():
                return UpdatePatientSerializer
            elif user.groups.filter(name='lab attendant'):
                return UpdateHealthProfileSerializer
        return None
    
    def get(self, request, *args, **kwargs):
        queryset = Patient.objects.all()  
        serializer_class = self.get_serializer_class()
        if serializer_class is None:
            return Response(status=405)  # Return HTTP 405 Method Not Allowed
        serializer = serializer_class(queryset,context={'request': request}, many= True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = serializer_class(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)








class DetailedView(APIView):

    permission_classes = [permissions.IsAuthenticated]
    

    def get_object(self, pk):
        try:
            return Patient.objects.get(pk=pk)
            
        except Patient.DoesNotExist:
            raise Http404


    def get_serializer_class(self):    # Get serializer class
        user = self.request.user    
        user = User.objects.get(username=user)           # Get user's object and 
        if self.request.method == 'GET':
            if user.groups.filter(name='record clerk').exists():        # it's group passed a condition to view
                return RClerkPatientSerializer      # just a few fields we've defined in it's serializer
            return FullPatientSerializer
        elif self.request.method == 'PUT':
            if not user.groups.filter(name='lab attendant').exists():
                return None
        return UpdateHealthProfileSerializer
    
    def get(self, request, pk, **kwargs):
        queryset = self.get_object(pk=pk)
        serializer_class = self.get_serializer_class()
        if serializer_class is None:
            return Response(status=405)  # Return HTTP 405 Method Not Allowed
        serializer = serializer_class(queryset, context={'request': request})
        return Response(serializer.data)
    
    def put(self, request, pk, **kwargs):
        queryset = self.get_object(pk=pk)
        serializer_class = self.get_serializer_class()
        if serializer_class is None:
            return Response({"error": "You are not allowed to update medical details."},status=405)  # Return HTTP 405 Method Not Allowed
        serializer = serializer_class(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, **kwargs):
        queryset = self.get_object(pk)
        user = self.request.user
        user = User.objects.get(username=user)   
        if user.groups.filter(name= 'medical clerk').exists() or is_staff:
            queryset.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=405) 
