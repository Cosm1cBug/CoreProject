# Generated by Django 4.0.4 on 2022-05-25 01:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0005_alter_user_kitsu"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="kitsu",
            field=models.JSONField(blank=True, default=dict, null=True),
        ),
    ]
