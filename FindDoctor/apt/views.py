from django.shortcuts import render, get_object_or_404
from hms.models import Hospital, Doctor
from hms.forms import UserForm
from .models import Appointment
from .forms import AppointmentForm

# Create your views here.

def make_appointment(request):
    form = AppointmentForm(request.POST or None, request.FILES or None)
    #appointments = Appointment.objects.all()
    if form.is_valid():
        appointment = form.save(commit=False)
        '''
        for a in appointments:
            if appointment.date is not a.date:
                break
            else:
                return render(request, 'apt/apt_failed.html')
        '''
        appointment.save()
        return render(request, 'apt/apt_success.html', {'appointment': appointment})
    return render(request, 'apt/appointment.html', {'form': form})

def apt_success(request):
    return render(request, 'apt/apt_success.html')
