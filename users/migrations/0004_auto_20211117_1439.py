# Generated by Django 3.2.8 on 2021-11-17 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20211117_1428'),
    ]

    operations = [
        migrations.AddField(
            model_name='details',
            name='first_name',
            field=models.CharField(default='r', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='details',
            name='las_name',
            field=models.CharField(default='Khan', max_length=100),
            preserve_default=False,
        ),
    ]
