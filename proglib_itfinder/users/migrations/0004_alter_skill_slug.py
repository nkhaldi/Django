# Generated by Django 4.0.6 on 2022-07-09 15:10

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0003_skill_slug"),
    ]

    operations = [
        migrations.AlterField(
            model_name="skill",
            name="slug",
            field=models.SlugField(),
        ),
    ]
