# Generated by Django 4.0.4 on 2022-04-23 16:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('philosophers', '0002_rename_philosophers_philosopher'),
        ('philosophy', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='philosophy',
            name='Philosopher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='books', to='philosophers.philosopher'),
        ),
    ]