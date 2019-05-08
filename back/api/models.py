from django.db import models

class User(models.Model):
	username = models.CharField(max_length=40)
	email = models.EmailField(unique=True, primary_key=True)
	password = models.CharField(max_length=20)

class Review(models.Model):
	review = models.CharField(max_length=1000)
	rating = models.IntegerField()
	author = models.CharField(max_length=30)
	submissionDate = models.DateField()

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


class FlightList(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    def to_json(self):
        return {
            'name': self.name,
            'id': self.id,
        }

class HotelList(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    def to_json(self):
        return {
            'name': self.name,
            'id': self.id,
        }