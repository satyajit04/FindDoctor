from django.db import models
from hms.models import Hospital, Doctor

# Create your models here.

class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor)
    patient_name = models.CharField(max_length=200)
    date = models.DateTimeField()

    def __str__(self):
        return self.patient_name + ' - ' + str(self.id) + ' - ' + self.doctor.name
