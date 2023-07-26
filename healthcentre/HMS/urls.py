from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from HMS.views import PatientRecordClerkView, PatientMedClerkView, PatientLaboratoristView
#RetrieveRecordClerkView

urlpatterns = [
    path('api/record-clerk/patients/', PatientRecordClerkView.as_view(), name='record-clerk-view'),
    path('api/med-clerk/patients/', PatientMedClerkView.as_view(), name='med-clerk-view'),
    path('api/laboratorist/patients/<int:pk>/', PatientLaboratoristView.as_view(), name='lab-attendant-view'),
  #  path('api/patients/<str:matric_No>/<str:healthcentre_No>/', RetrieveRecordClerkView.as_view(),name = 'record-clerk-search-view')
]