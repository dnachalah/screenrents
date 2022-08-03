from django.db import models

# Create your models here.

class Rentalsapp(models.Model):
    lastname = models.CharField(max_length=255)
    firstname = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    dob = models.CharField(max_length=255)
    age = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

class screenbooks(models.Model):
    id = models.IntegerField(primary_key = True)
    screenname = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    date_added = models.CharField(max_length=255)
    added_by = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    picture = models.ImageField(upload_to="media")
    class Meta:
        db_table = "screen_bookings"