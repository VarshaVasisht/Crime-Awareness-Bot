# Generated by Django 3.1.7 on 2021-05-06 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('police', '0006_auto_20210506_2250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compliant',
            name='url',
            field=models.CharField(max_length=500),
        ),
    ]
