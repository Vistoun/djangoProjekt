# Generated by Django 3.2 on 2021-06-14 07:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('opravy', '0007_remove_oprava_model'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='oprava',
            name='zakaznik',
        ),
    ]
