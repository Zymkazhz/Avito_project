# Generated by Django 3.2.16 on 2023-01-02 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appsite', '0004_scooters_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=50)),
            ],
        ),
    ]
