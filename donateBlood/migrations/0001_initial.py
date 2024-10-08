# Generated by Django 5.1 on 2024-08-15 14:18

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='donor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=200)),
                ('Phone', models.CharField(max_length=10)),
                ('Email', models.EmailField(blank=True, max_length=200, null=True)),
                ('Address', models.CharField(max_length=350)),
                ('BloodType', models.CharField(choices=[('a+', 'A+'), ('b+', 'B+'), ('o+', 'O+'), ('ab+', 'AB+'), ('a-', 'A-'), ('b-', 'B-'), ('o-', 'O-'), ('ab-', 'AB-')], max_length=9)),
                ('age', models.IntegerField(validators=[django.core.validators.MaxValueValidator(65), django.core.validators.MinValueValidator(18)])),
                ('medical_ailments', models.CharField(blank=True, max_length=500, null=True)),
                ('verify', models.BooleanField(blank=True, null=True)),
            ],
        ),
    ]
