# Generated by Django 4.1.7 on 2023-03-08 12:17

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("anime", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="animethememodel",
            name="type",
            field=models.CharField(default="", max_length=50),
        ),
    ]