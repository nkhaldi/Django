# Generated by Django 4.1.2 on 2023-04-16 14:08

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("orders", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="status",
            field=models.SmallIntegerField(
                choices=[
                    (0, "Создан"),
                    (1, "Оплачен"),
                    (2, "В пути"),
                    (3, "Доставлен"),
                ],
                default=0,
            ),
        ),
    ]
