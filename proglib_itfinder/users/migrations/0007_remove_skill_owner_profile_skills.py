# Generated by Django 4.0.6 on 2022-07-10 13:34

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0006_remove_profile_skills"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="skill",
            name="owner",
        ),
        migrations.AddField(
            model_name="profile",
            name="skills",
            field=models.ManyToManyField(blank=True, to="users.skill"),
        ),
    ]
