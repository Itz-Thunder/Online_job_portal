# Generated by Django 4.1 on 2022-09-01 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jamapp', '0005_jobs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobs',
            name='posteddate',
            field=models.CharField(max_length=40),
        ),
    ]
