# Generated by Django 3.2.8 on 2021-11-17 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='details',
            name='campus',
            field=models.CharField(default='Blacksburg', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='details',
            name='first_name',
            field=models.CharField(default='Rehan', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='details',
            name='last_name',
            field=models.CharField(default='Khan', max_length=100),
            preserve_default=False,
        ),
    ]
