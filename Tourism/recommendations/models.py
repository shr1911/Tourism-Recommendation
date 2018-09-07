from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractUser
from django.contrib.auth.models import User

# Create your models here.

class UserSurvey(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    home_delivery = models.CharField(max_length=100, help_text='100 characters max.')
    smoking = models.CharField(max_length=100, help_text='100 characters max.')
    alcohol = models.CharField(max_length=100, help_text='100 characters max.')
    wifi = models.CharField(max_length=100, help_text='100 characters max.')
    valetparking = models.CharField(max_length=100, help_text='100 characters max.')
    rooftop = models.CharField(max_length=100, help_text='100 characters max.')

class Restaurant(models.Model):
	rname = models.CharField(max_length=100)
	latitude = models.FloatField()
	longitude = models.FloatField()
	address = models.CharField(max_length=300)
	area = models.CharField(max_length=30)
	city = models.CharField(max_length=30)
	price = models.IntegerField(default=0)
	rating = models.FloatField(default=0.0)
	homedelivery = models.CharField(max_length=5)
	smoking = models.CharField(max_length=5)
	alcohol = models.CharField(max_length=5)
	wifi = models.CharField(max_length=5)
	valetparking = models.CharField(max_length=5)
	rooftop = models.CharField(max_length=5)

class Cuisine(models.Model):
	rid = models.ForeignKey(Restaurant, on_delete=models.CASCADE,)
	cuisine = models.CharField(max_length=30)

class Payment(models.Model):
	rid = models.ForeignKey(Restaurant, on_delete=models.CASCADE,)
	payment = models.CharField(max_length=40)

class Timing(models.Model):
	rid = models.ForeignKey(Restaurant, on_delete=models.CASCADE,)
	day = models.CharField(max_length=40)
	timing = models.CharField(max_length=40)
	starttime = models.CharField(max_length=40)
	endtime = models.CharField(max_length=40)

class CusineTiming(models.Model):
	cuisine = models.CharField(max_length=40)
	starttime = models.CharField(max_length=40)
	endtime = models.CharField(max_length=40)
