# Generated by Django 4.1.5 on 2023-01-05 21:05

import django.core.validators
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Address",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("street", models.CharField(max_length=80)),
                (
                    "zip_code",
                    models.CharField(
                        max_length=8,
                        validators=[
                            django.core.validators.MinLengthValidator(8),
                            django.core.validators.MaxLengthValidator(8),
                        ],
                    ),
                ),
                ("district", models.CharField(max_length=20)),
                ("city", models.CharField(max_length=80)),
                ("number", models.IntegerField()),
                ("state", models.CharField(max_length=50)),
            ],
        ),
    ]
