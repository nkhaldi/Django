# Generated by Django 4.0.6 on 2022-07-10 13:10

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0005_profile_skills"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="profile",
            name="skills",
        ),
    ]
