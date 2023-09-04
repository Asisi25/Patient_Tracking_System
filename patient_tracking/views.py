from .models import *
from django.shortcuts import render
from django.urls import reverse
from django.views.generic.edit import  FormView, CreateView, UpdateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

# Create your views here.

def dashboard(request): 
    data = {
        'patients': Patient.objects.all(),
        'appointments': Appointment.objects.all(),
        'medical_histories': MedicalHistory.objects.all(),
        'prescriptions': Prescription.objects.all()
    }
    return render(request, 'patient_tracking/dashboard.html', data)

class PatientListView(ListView): 
    model = Patient 
    paginate_by = 100  # if pagination is desired
    template_name = 'patient_tracking/patients/patient_list.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

class PatientCreateView(CreateView): 
    model = Patient 
    fields = '__all__'
    template_name = 'patient_tracking/patients/patient_form.html'

class PatientDetailView(DetailView):
    model = Patient
    template_name = 'patient_tracking/patients/patient_detail.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context
class PatientUpdateView(UpdateView): 
    model = Patient 
    fields = '__all__'
    template_name = 'patient_tracking/patients/patient_form.html'

class MedicalHistoryListView(ListView): 
    model = MedicalHistory 
    paginate_by = 100  # if pagination is desired
    template_name = 'patient_tracking/medical_histories/medical_history_list.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context
class MedicalHistoryCreateView(CreateView): 
    model = MedicalHistory 
    fields = '__all__'
    template_name = 'patient_tracking/medical_histories/medical_history_form.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context
    
class MedicalHistoryDetailView(DetailView):
    model = MedicalHistory
    template_name = 'patient_tracking/medical_histories/medical_history_detail.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context
    
class MedicalHistoryUpdateView(UpdateView): 
    model = MedicalHistory 
    fields = '__all__'
    template_name = 'patient_tracking/medical_histories/medical_history_form.html'
