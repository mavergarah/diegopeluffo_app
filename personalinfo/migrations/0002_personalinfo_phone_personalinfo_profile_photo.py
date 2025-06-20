# Generated by Django 4.2.16 on 2025-05-25 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personalinfo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='personalinfo',
            name='phone',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='personalinfo',
            name='profile_photo',
            field=models.ImageField(blank=True, null=True, upload_to='uploads'),
        ),
    ]
