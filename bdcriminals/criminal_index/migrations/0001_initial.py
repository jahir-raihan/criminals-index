# Generated by Django 5.0.7 on 2024-08-03 17:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Criminal",
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
                ("criminal_name", models.CharField(max_length=50)),
                ("crime_location", models.CharField(max_length=250)),
                ("social_links", models.TextField()),
                ("crime_details", models.TextField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="Evidence",
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
                ("file", models.FileField(upload_to="evidence")),
                ("is_video", models.BooleanField(default=False)),
                (
                    "criminal",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="criminal_index.criminal",
                    ),
                ),
            ],
        ),
    ]
