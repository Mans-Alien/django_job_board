# Generated by Django 4.2.3 on 2023-08-08 21:44

import accounts.models
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0003_alter_profile_city_alter_profile_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="image",
            field=models.ImageField(
                blank=True,
                default="profile/default.png",
                upload_to=accounts.models.profile_image,
            ),
        ),
    ]
