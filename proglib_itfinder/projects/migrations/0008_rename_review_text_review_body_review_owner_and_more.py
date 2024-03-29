# Generated by Django 4.0.6 on 2022-07-13 15:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0012_message"),
        ("projects", "0007_alter_tag_slug"),
    ]

    operations = [
        migrations.RenameField(
            model_name="review",
            old_name="review_text",
            new_name="body",
        ),
        migrations.AddField(
            model_name="review",
            name="owner",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="users.profile",
            ),
        ),
        migrations.AlterUniqueTogether(
            name="review",
            unique_together={("owner", "project")},
        ),
    ]
