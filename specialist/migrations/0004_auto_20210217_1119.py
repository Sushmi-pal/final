# Generated by Django 2.2.3 on 2021-02-17 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('specialist', '0003_appointment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor_profile',
            name='nmc_num',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='doctor_profile',
            name='phone',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='doctor_profile',
            name='qualification',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='doctor_profile',
            name='speciality',
            field=models.CharField(max_length=50),
        ),
    ]
