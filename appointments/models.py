from django.db import models
from django.contrib.postgres.fields import ArrayField
from phone_field import PhoneField

# Create your models here.

class Appointment(models.Model):
    name         = models.CharField(max_length=256)
    phone        = PhoneField(help_text='Contact phone number')
    email        = models.EmailField()
    details      = models.TextField()
    completed    = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Quote(models.Model):
    name          = models.CharField(max_length=256)
    phone         = models.BigIntegerField()
    email         = models.EmailField()
    amt_rooms     = models.IntegerField()
    rooms         = ArrayField(models.CharField(max_length=256),size=6)
    property_type = models.CharField(max_length=256)
    category      = models.CharField(max_length=128)
    area          = models.FloatField()
    address       = models.TextField()
    budget        = models.IntegerField()
    pincode       = models.IntegerField()
    date_created  = models.DateTimeField(auto_now_add=True)
    date_updated  = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name