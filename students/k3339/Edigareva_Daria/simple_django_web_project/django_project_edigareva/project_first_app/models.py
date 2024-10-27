from django.db import models


class CarOwner(models.Model):
    last_name = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    birth_date = models.DateTimeField(null=True, blank=True)


class Car(models.Model):
    registration_number = models.CharField(max_length=15, unique=True)
    make = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    color = models.CharField(max_length=30, null=True, blank=True)


class DrivingLicense(models.Model):
    owner = models.ForeignKey(CarOwner, on_delete=models.CASCADE)
    license_number = models.CharField(max_length=10, unique=True)
    license_type = models.CharField(max_length=10)
    issue_date = models.DateTimeField()


class Ownership(models.Model):
    car_owner = models.ForeignKey(CarOwner, on_delete=models.CASCADE, null=True)
    car = models.ForeignKey(Car, on_delete=models.CASCADE, null=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(null=True, blank=True)
