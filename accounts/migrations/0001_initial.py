# Generated by Django 4.1.5 on 2023-01-10 14:30

import django.core.validators
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Account",
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
                (
                    "account_number",
                    models.CharField(
                        max_length=20,
                        validators=[
                            django.core.validators.MaxLengthValidator(20),
                            django.core.validators.MinLengthValidator(3),
                        ],
                    ),
                ),
                (
                    "agency",
                    models.CharField(
                        max_length=5,
                        validators=[
                            django.core.validators.MaxLengthValidator(5),
                            django.core.validators.MinLengthValidator(3),
                        ],
                    ),
                ),
                (
                    "type",
                    models.CharField(
                        choices=[("Current account", "Cc"), ("Savings account", "Cp")],
                        default="Current account",
                        max_length=20,
                    ),
                ),
                (
                    "code",
                    models.CharField(
                        default=None,
                        max_length=3,
                        null=True,
                        validators=[
                            django.core.validators.MaxLengthValidator(3),
                            django.core.validators.MinLengthValidator(3),
                        ],
                    ),
                ),
                ("balance", models.DecimalField(decimal_places=2, max_digits=15)),
                (
                    "overdraft_limit",
                    models.DecimalField(decimal_places=2, max_digits=15),
                ),
            ],
        ),
    ]
