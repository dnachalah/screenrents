# Generated by Django 4.0.6 on 2022-07-29 14:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rentalsapp', '0012_screenbook_delete_screenbookings'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='screenbook',
            new_name='screenbooks',
        ),
        migrations.AlterModelTable(
            name='screenbooks',
            table='screen_bookings',
        ),
    ]