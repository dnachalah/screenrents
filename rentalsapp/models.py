from django.db import models

# Create your models here.

class Rentalsapp(models.Model):
    lastname = models.CharField(max_length=255)
    firstname = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    profile_picture = models.ImageField(null=True, blank=True)
    class Meta:
        db_table = "rentalsapp_rentalsapp"

class screens(models.Model):
    id = models.IntegerField(primary_key = True)
    screenname = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    date_added = models.CharField(max_length=255)
    added_by = models.CharField(max_length=255)
    updated_by = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    picture = models.ImageField(upload_to='screens')
    class Meta:
        db_table = "screens_list"

class screenbookings(models.Model):
    id = models.IntegerField(primary_key = True)
    user_id = models.IntegerField(null = True)
    screen_id = models.IntegerField(null = True)
    date_added = models.CharField(max_length=255)
    date_for_pickup = models.CharField(max_length=255)
    date_for_return = models.CharField(max_length=255)
    added_by = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    class Meta:
        db_table = "screens"

class admin(models.Model):
    id = models.IntegerField(primary_key = True)
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    profile_picture = models.ImageField(null=True, blank=True)
    class Meta:
        db_table = "admin_rentalsapp"



class contacts(models.Model):
    id = models.IntegerField(primary_key = True)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    message = models.CharField(max_length=255)
    class Meta:
        db_table = "contact_record"
