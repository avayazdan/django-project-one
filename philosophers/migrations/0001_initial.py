# Generated by Django 4.0.4 on 2022-04-21 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Philosophers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('birth_place', models.CharField(max_length=50)),
                ('works', models.CharField(max_length=50)),
                ('branch', models.CharField(max_length=50)),
                ('image', models.CharField(max_length=300)),
                ('time_period', models.CharField(max_length=50)),
            ],
        ),
    ]
