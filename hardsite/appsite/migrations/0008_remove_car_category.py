# Generated by Django 3.2.16 on 2023-01-02 16:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appsite', '0007_car_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='category',
        ),
    ]
