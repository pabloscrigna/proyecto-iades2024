# Generated by Django 5.1.2 on 2024-10-30 23:28

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("iades", "0009_oyente_alter_profesor_options"),
    ]

    operations = [
        migrations.AddField(
            model_name="curso",
            name="cantidad",
            field=models.IntegerField(default=0),
        ),
    ]
