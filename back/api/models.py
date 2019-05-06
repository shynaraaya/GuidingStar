from django.db import models

class User(models.Model):
	username = models.CharField(max_length=40)
	email = models.CharField(max_length=35, unique=True, primary_key=True)
	password = models.CharField(max_length=20)

class Flight(models.Model):
	companyName = models.CharField(max_length=30)
	sourceLocation = models.CharField(max_length=30)
	destinationLocation = models.CharField(max_length=30)
	departureDate = models.DateField()
	departureTime = models.TimeField()
	fareEconomy = models.DecimalField(max_digits=6,decimal_places=2)
	fareBusiness = models.DecimalField(max_digits=6,decimal_places=2)
	fareFirst = models.DecimalField(max_digits=6,decimal_places=2)
	numSeatsRemainingEconomy = models.IntegerField()
	numSeatsRemainingBusiness = models.IntegerField()
	numSeatsRemainingFirst = models.IntegerField()

class Hotel(models.Model):
	dailyCost = models.DecimalField(max_digits=6,decimal_places=2)
	address = models.CharField(max_length=30)
	city = models.CharField(max_length=30)
	companyName = models.CharField(max_length=30,default='hotel')