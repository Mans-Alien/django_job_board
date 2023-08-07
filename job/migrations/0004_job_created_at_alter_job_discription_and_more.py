# Generated by Django 4.2.3 on 2023-08-06 18:03

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("job", "0003_job_discription"),
    ]

    operations = [
        migrations.AddField(
            model_name="job",
            name="created_at",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name="job",
            name="discription",
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name="job",
            name="job_type",
            field=models.CharField(
                blank=True,
                choices=[("FT", "Full Time"), ("PT", "Part Time")],
                max_length=2,
                null=True,
            ),
        ),
    ]
