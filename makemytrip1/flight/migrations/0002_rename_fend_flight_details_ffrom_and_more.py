# Generated by Django 4.0.10 on 2023-03-08 06:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flight', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='flight_details',
            old_name='fend',
            new_name='ffrom',
        ),
        migrations.RenameField(
            model_name='flight_details',
            old_name='fstart',
            new_name='fto',
        ),
    ]