# Generated by Django 5.0.4 on 2024-06-10 12:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_school_sdate_of_birth'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='school',
            name='Sdate_of_birth',
        ),
    ]