# Generated by Django 4.1.6 on 2023-02-10 21:24

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("portfolio", "0005_job_resume_bullet"),
    ]

    operations = [
        migrations.AddField(
            model_name="resume",
            name="summary",
            field=models.TextField(blank=True, max_length=240, null=True),
        ),
    ]
