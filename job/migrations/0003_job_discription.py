# Generated by Django 4.2.3 on 2023-08-06 17:59

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("job", "0002_job_job_type"),
    ]

    operations = [
        migrations.AddField(
            model_name="job",
            name="discription",
            field=models.TextField(max_length=1000, null=True),
        ),
    ]
