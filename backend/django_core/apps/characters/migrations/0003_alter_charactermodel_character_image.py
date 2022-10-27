# Generated by Django 4.1.1 on 2022-09-05 13:21

import apps.characters.models
import core.storages

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("characters", "0002_alter_charactermodel_mal_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="charactermodel",
            name="character_image",
            field=models.ImageField(
                blank=True,
                default=None,
                null=True,
                storage=core.storages.OverwriteStorage(),
                upload_to=apps.characters.models.FileField.anime_charater,
            ),
        ),
    ]