from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import PatientListView, DetailedView

urlpatterns = [
    path('patients/', PatientListView.as_view(), name = 'patient'),
    path('patients/<int:pk>/', DetailedView.as_view(), name='patient-detail'),
    
]