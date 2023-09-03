from django.shortcuts import render
from django.views.generic.edit import  FormView, CreateView, UpdateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .forms import PatientForm
from .models import *

# Create your views here.

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