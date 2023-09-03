from django.urls import path
app_name = 'patient_tracking'

from . import views
urlpatterns=[
    path('patients/', views.PatientListView.as_view(), name='patients-list'),
    path('patients/create/', views.PatientCreateView.as_view(), name='patients-create'),
    path('patients/<pk>/', views.PatientDetailView.as_view(), name='patients-detail'),
    path('patients/<pk>/edit/', views.PatientUpdateView.as_view(), name='patients-edit'),
]