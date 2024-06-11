# Generated by Django 5.0.4 on 2024-06-10 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('Sname', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('Sage', models.PositiveIntegerField()),
                ('Scollege', models.CharField(max_length=100)),
                ('Slocation', models.CharField(max_length=100)),
                ('Sdate_of_birth', models.DateField()),
            ],
        ),
    ]
