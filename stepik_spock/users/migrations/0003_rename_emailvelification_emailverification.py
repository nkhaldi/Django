# Generated by Django 3.2.13 on 2023-02-12 20:52

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0002_auto_20230212_2021"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="EmailVelification",
            new_name="EmailVerification",
        ),
    ]
