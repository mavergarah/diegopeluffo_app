# Generated by Django 4.2.16 on 2025-06-20 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personalinfo', '0007_downloaddocument_linkinterest_kind_of_link_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='researchline',
            name='kind_of_reseach',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Current'), (2, 'Past')], default=200, verbose_name='Kind of Research'),
        ),
    ]
