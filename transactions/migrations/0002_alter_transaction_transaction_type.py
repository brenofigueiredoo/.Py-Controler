# Generated by Django 4.1.5 on 2023-01-05 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("transactions", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="transaction",
            name="transaction_type",
            field=models.CharField(
                choices=[("payment", "Pmt"), ("receipt", "Rct")], max_length=7
            ),
        ),
    ]
