# Generated by Django 3.1.7 on 2021-05-18 09:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('police', '0008_alerts'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alerts',
            name='alert',
        ),
        migrations.RemoveField(
            model_name='alerts',
            name='lanndmark',
        ),
        migrations.RemoveField(
            model_name='alerts',
            name='uid',
        ),
    ]
