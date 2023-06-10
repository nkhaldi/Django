# Generated by Django 4.0.6 on 2022-07-09 14:12

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("projects", "0003_remove_project_feature_image_project_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="project",
            name="image",
            field=models.ImageField(
                blank=True,
                default="project_images/default.jpg",
                null=True,
                upload_to="project_images",
            ),
        ),
    ]
