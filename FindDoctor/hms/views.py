from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .forms import UserForm
from .models import Hospital, Doctor
from apt.models import Appointment
import operator

# Create your views here.

def index(request):
    if not request.user.is_authenticated():
        return render(request, 'hms/login.html')
    else:
        return render(request, 'hms/index.html')

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request, 'hms/index.html')
            else:
                return render(request, 'hms/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'hms/login.html', {'error_message': 'Invalid login'})
    return render(request, 'hms/login.html')


def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'hms/login.html', context)


def register(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request, 'hms/index.html')
    context = {
        "form": form,
    }
    return render(request, 'hms/register.html', context)

def hospital_index(request):
    hospitals = sorted(Hospital.objects.all(),key=operator.attrgetter('hospital_name'))
    #doctors = sorted(Doctor.objects.all(),key=operator.attrgetter('name'))
    #context = {'hospitals': hospitals}
    #hospitals = Hospital.objects.all()
    doctors = Doctor.objects.all()
    query = request.GET.get("q")
    if query:
        doctors = doctors.filter(
            Q(speciality__icontains=query)|Q(health_issue__icontains=query)|Q(hospital__hospital_name__icontains=query)
        ).distinct()
        return render(request,'hms/search.html',{'doctors': doctors})
    else:
        return render(request,'hms/index.html', {'hospitals': hospitals})

def hospital_details(request,pk):
    hospital = get_object_or_404(Hospital, pk=pk)
    return render(request,'hms/hospital_details.html', {'hospital': hospital})

def doctor_index(request):
    doctors = sorted(Doctor.objects.all(),key=operator.attrgetter('name'))
    return render(request,'hms/doctor_index.html',{'doctors': doctors})

def doctor_details(request,id):
    doctor = get_object_or_404(Doctor, id=id)
    appointments = sorted(Appointment.objects.filter(doctor__id=id),key=operator.attrgetter('date'))
    #appointments = Appointment.objects.all()
    return render(request,'hms/doctor_details.html',{
        'doctor': doctor,
        'appointments': appointments,
    })

def hospital_doctorlist(request, pk, id):
    hospital = get_object_or_404(Hospital, pk=pk)
    doctor = hospital.doctor_set.get(id=id)
    appointments = sorted(Appointment.objects.filter(doctor__id=id),key=operator.attrgetter('date'))
    return render(request,'hms/doctor_details.html', {
        'doctor': doctor,
        'appointments': appointments,
    })
