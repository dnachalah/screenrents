# Generated by Django 4.0.6 on 2022-08-02 10:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rentalsapp', '0017_alter_screenbooks_picture'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='screenbooks',
            name='picture',
        ),
    ]