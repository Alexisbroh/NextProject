from django.db import models


# Create your models here.

class Student(models.Model):
    nameEstudiante = models.CharField(max_length=100)
    apellidoEstudiante = models.CharField(max_length=100)
    semester = models.IntegerField()




class Patient(models.Model):
    namePatient = models.CharField(max_length=100)
    lastnamePatient = models.CharField(max_length=100)
    healthCare = models.CharField(max_length=15)
    datebirth = models.CharField(max_length=15)

   
    student = models.ForeignKey(Student, on_delete=models.CASCADE) 

class Tratamientos(models.Model):
    nombreTratamiento = models.CharField(max_length=100)    