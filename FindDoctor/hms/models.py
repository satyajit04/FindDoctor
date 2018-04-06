from django.db import models
from django.contrib.auth.models import Permission, User
from multiselectfield import MultiSelectField

# Create your models here.

class Hospital(models.Model):
    hospital_name = models.CharField(max_length=500)
    area = models.CharField(max_length=100)
    address = models.CharField(max_length=500)
    image = models.FileField()

    def __str__(self):
        return self.hospital_name

class Doctor(models.Model):

    HEALTH_ISSUES = (
        ('chest pain', 'chest pain'),
        ('suffocation', 'suffocation'),
        ('stomachache', 'stomachache'),
        ('toothache', 'toothache'),
        ('fever', 'fever'),
        ('allergy', 'allergy'),
        ('std', 'std'),
        ('constipation', 'constipation'),
        ('diarrhea', 'diarrhea'),
        ('dysentery', 'dysentery'),
        ('ulcer', 'ulcer'),
        ('child disease', 'child disease'),
        ('gastric', 'gastric'),
        ('marital issues', 'marital issues'),
        ('headache', 'headache'),
        ('mental condition', 'mental condition'),
        ('broken bone', 'broken bone'),
        ('fracture', 'fracture'),
        ('stroke', 'stroke'),
        ('nervous problems', 'nervous problems'),
        ('seizure', 'seizure'),
        ('swallowing', 'swallowing'),
    )

    SPECIALIZATION = (
        ('Cardiologist', 'Cardiologist'),
        ('Medicine', 'Medicine'),
        ('Dermatologist', 'Dermatologist'),
        ('Pediatrician', 'Pediatrician'),
        ('Gastroenterologist', 'Gastroenterologist'),
        ('Gynecologist', 'Gynecologist'),
        ('Neurologist', 'Neurologist'),
        ('Orthopedic', 'Orthopedic'),
        ('Psychiatrist', 'Psychiatrist'),
        ('Dentist', 'Dentist'),
    )

    name = models.CharField(max_length=200)
    hospital = models.ForeignKey(Hospital)
    speciality = models.CharField(max_length=50,choices=SPECIALIZATION)
    health_issue = MultiSelectField(max_length=500,choices=HEALTH_ISSUES)
    dp = models.FileField()

    def __str__(self):
        return self.name + ' - ' + self.speciality
