# Generated by Django 3.2.8 on 2021-11-17 21:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_details'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Details',
        ),
    ]