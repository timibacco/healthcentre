from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from HMS.views import PatientRecordClerkView, PatientMedClerkView, PatientLabAttendantView

urlpatterns = [
    path('record-clerk/patientslist', PatientRecordClerkView.as_view(), name='record-clerk-view'),
    path('med-clerk/patientslist/', PatientMedClerkView.as_view(), name='med-clerk-view'),
    path('lab-attendant/<int:pk>/', PatientLabAttendantView.as_view(), name='lab-attendant-view'),
]