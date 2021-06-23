# Generated by Django 3.1.7 on 2021-05-05 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('police', '0004_auto_20210504_1941'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='compliant',
            name='screenshot',
        ),
        migrations.AddField(
            model_name='compliant',
            name='lat',
            field=models.CharField(default='none', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='compliant',
            name='lon',
            field=models.CharField(default='none', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='compliant',
            name='url',
            field=models.CharField(default='none', max_length=60),
            preserve_default=False,
        ),
    ]
