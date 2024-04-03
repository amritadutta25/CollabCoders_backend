# Generated by Django 5.0.3 on 2024-04-03 00:37

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Meeting",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("host_name", models.CharField(max_length=100)),
                ("title", models.TextField()),
                ("description", models.TextField()),
                ("technology", models.CharField(max_length=100)),
                ("date", models.DateField()),
                ("time", models.TimeField()),
                ("duration", models.FloatField()),
                ("skill_level", models.CharField(max_length=100)),
                ("session_link", models.CharField(max_length=100)),
                ("status", models.CharField(max_length=100)),
            ],
        ),
    ]