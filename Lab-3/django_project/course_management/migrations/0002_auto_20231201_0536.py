# Generated by Django 3.2.3 on 2023-12-01 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_management', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumno',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='asignatura',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
