# Generated by Django 5.1.2 on 2024-10-30 22:36

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("iades", "0007_profesores"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Cursos",
            new_name="Curso",
        ),
        migrations.RenameModel(
            old_name="Estudiantes",
            new_name="Estudiante",
        ),
        migrations.RenameModel(
            old_name="Profesores",
            new_name="Profesor",
        ),
    ]
