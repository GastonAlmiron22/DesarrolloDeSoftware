from django.db import models

#Modelo de Vehiculo
class Car(models.Model):
    brand = models.CharField(max_length=30)
    model = models.CharField(max_length=30)
    value = models.IntegerField()
    licencePlate = models.CharField(max_length=30)

#Modelo de conductor
class Driver(models.Model):
    name = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    dateOfBirth = models.DateField()
    dni = models.IntegerField()

#Modelo de escuela
class School(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    schoolCode = models.IntegerField(default=0)

#Modelo de viaje
class Trip(models.Model):
    driverId = models.ForeignKey(Driver, on_delete=models.CASCADE)
    carId = models.ForeignKey(Car, on_delete=models.CASCADE)
    tripDate = models.DateField()

#Modelo de viaje-escuela
class SchoolTrip(models.Model):
    tripId = models.ForeignKey(Trip, on_delete=models.CASCADE)
    schoolId = models.ForeignKey(School, on_delete=models.CASCADE)
    tripSchoolCode = models.IntegerField(default=0)

#Modelo de estudiante
class Student(models.Model):
    name = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    dateOfBirth = models.DateField()
    dni = models.IntegerField()
    studentCode = models.IntegerField(default=0)
    schoolId = models.ForeignKey(School, on_delete=models.CASCADE)

class StudentTrip(models.Model):
    studentId = models.ForeignKey(Student, on_delete=models.CASCADE)
    tripId = models.ForeignKey(Trip, on_delete=models.CASCADE)
    studentTripCode = models.IntegerField(default=0)