from django.urls import path
app_name = 'patient_tracking'

from . import views
urlpatterns=[
    path('', views.dashboard, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('medical-histories/', views.MedicalHistoryListView.as_view(), name='medical-histories-list'),
    path('medical-histories/create/', views.MedicalHistoryCreateView.as_view(), name='medical-histories-create'),
    path('medical-histories/<pk>/', views.MedicalHistoryDetailView.as_view(), name='medical-histories-detail'),
    path('medical-histories/<pk>/edit', views.MedicalHistoryUpdateView.as_view(), name='medical-histories-edit'),

    path('patients/', views.PatientListView.as_view(), name='patients-list'),
    path('patients/create/', views.PatientCreateView.as_view(), name='patients-create'),
    path('patients/<pk>/', views.PatientDetailView.as_view(), name='patients-detail'),
    path('patients/<pk>/edit/', views.PatientUpdateView.as_view(), name='patients-edit'),
]