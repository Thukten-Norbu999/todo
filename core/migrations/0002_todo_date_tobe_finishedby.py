# Generated by Django 5.0.4 on 2024-05-02 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='date_toBe_finishedBy',
            field=models.DateField(auto_now=True, verbose_name='Date to be finished by'),
        ),
    ]
