from django import forms
from hms.forms import UserForm
from .models import Appointment

class AppointmentForm(forms.ModelForm):

    class Meta:
        model = Appointment
        fields = ['doctor', 'patient_name', 'date']
