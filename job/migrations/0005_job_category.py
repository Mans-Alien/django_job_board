# Generated by Django 4.2.3 on 2023-07-23 19:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("job", "0004_category"),
    ]

    operations = [
        migrations.AddField(
            model_name="job",
            name="category",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="job.category",
            ),
            preserve_default=False,
        ),
    ]