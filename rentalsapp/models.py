from django.db import models

# Create your models here.

class Rentalsapp(models.Model):
    id = models.IntegerField(primary_key = True)
    lastname = models.CharField(max_length=255)
    firstname = models.CharField(max_length=255)
    email = models.CharField(max_length=4294967295)
    password = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    profile_picture = models.ImageField(null=True, blank=True)
    class Meta:
        db_table = "users"

class subscription(models.Model):
    id = models.IntegerField(primary_key = True)
    email = models.CharField(max_length=255)
    class Meta:
        db_table = "subscribed_emails"

class categories(models.Model):
    id = models.IntegerField(primary_key = True)
    category = models.CharField(max_length=255)
    class Meta:
        db_table = "categoryy"

class brands(models.Model):
    id = models.IntegerField(primary_key = True)
    brand = models.CharField(max_length=255)
    class Meta:
        db_table = "brandd"

class screens(models.Model):
    id = models.IntegerField(primary_key = True)
    screenname = models.CharField(max_length=4294967295)
    description = models.CharField(max_length=4294967295)
    date_added = models.CharField(max_length=255)
    added_by = models.CharField(max_length=255)
    updated_by = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    picture = models.ImageField(upload_to='screens')
    category_id = models.CharField(max_length=255)
    brand_id = models.CharField(max_length=255)
    dimension = models.CharField(max_length=4294967295)
    quantity = models.CharField(max_length=255)
    short_description = models.CharField(max_length=100000000)
    class Meta:
        db_table = "screenss"

class screenbookings(models.Model):
    id = models.IntegerField(primary_key = True)
    user_id = models.CharField(max_length=255)
    screen_id = models.CharField(max_length=255)
    date_added = models.CharField(max_length=255)
    date_for_pickup = models.CharField(max_length=255)
    date_for_return = models.CharField(max_length=255)
    added_by = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    user_email = models.CharField(max_length=255)
    screen_price = models.CharField(max_length=255)
    current_timee = models.CharField(max_length=255)
    class Meta:
        db_table = "screens_bookings"

class admin(models.Model):
    id = models.IntegerField(primary_key = True)
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    email = models.CharField(max_length=4294967295)
    password = models.CharField(max_length=255)
    profile_picture = models.ImageField(null=True, blank=True)
    class Meta:
        db_table = "admins"



class contacts(models.Model):
    id = models.IntegerField(primary_key = True)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=4294967295)
    phone = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    message = models.CharField(max_length=255)
    class Meta:
        db_table = "contacts"


class transactions(models.Model):
    id = models.IntegerField(primary_key = True)
    order_id = models.CharField(max_length=255)
    user_id = models.CharField(max_length=255)
    user_email = models.CharField(max_length=4294967295)
    payment_date = models.CharField(max_length=255)
    amount_paid = models.CharField(max_length=255)
    transaction_key = models.CharField(max_length=255)
    class Meta:
        db_table = "transaction_details"