from django.db import models
from django.contrib.auth.models import User


class CategoryManager(models.Manager):
    def for_user(self, user):
        return self.filter(created_by=user)


class Review(models.Model):
    review = models.CharField(max_length=1000)
    rating = models.IntegerField(default=3)
    submissionDate = models.DateField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, default=2)
    objects = CategoryManager()

    class Meta:
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'

    def __str__(self):
        return '{}: {}, {}'.format(self.id, self.created_by, self.rating)

    def to_json(self):
        return {
            'id': self.id,
            'author': self.created_by,
            'rating': self.rating
        }


class Flight(models.Model):
    companyName = models.CharField(max_length=300)
    sourceLocation = models.CharField(max_length=30)
    destinationLocation = models.CharField(max_length=30)
    departureDate = models.DateField()
    departureTime = models.TimeField()
    fareEconomy = models.DecimalField(max_digits=6, decimal_places=2)
    fareBusiness = models.DecimalField(max_digits=6, decimal_places=2)
    fareFirst = models.DecimalField(max_digits=6, decimal_places=2)
    numSeatsRemainingEconomy = models.IntegerField()
    numSeatsRemainingBusiness = models.IntegerField()
    numSeatsRemainingFirst = models.IntegerField()

    class Meta:
        verbose_name = 'Flight'
        verbose_name_plural = 'Flights'

    def __str__(self):
        return '{}: {}, {}'.format(self.id, self.sourceLocation, self.destinationLocation)

    def to_json(self):
        return {
            'id': self.id,
            'Source': self.sourceLocation,
            'Destination': self.destinationLocation
        }


class Hotel(models.Model):
    dailyCost = models.DecimalField(max_digits=6, decimal_places=2)
    address = models.CharField(max_length=30)
    city = models.CharField(max_length=300)
    hotels = models.IntegerField(default=3)
    poster = models.CharField(max_length=999, default='poster')
    companyName = models.CharField(max_length=30, default='hotel')

    class Meta:
        verbose_name = 'Hotel'
        verbose_name_plural = 'Hotels'

    def __str__(self):
        return '{}: {}, {}'.format(self.id, self.companyName, self.city)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.companyName,
            'city': self.city
        }


