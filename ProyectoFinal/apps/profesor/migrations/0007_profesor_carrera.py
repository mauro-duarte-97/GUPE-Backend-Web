# Generated by Django 5.0 on 2024-05-26 22:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carrera', '0009_alter_carrera_img_perfil'),
        ('profesor', '0006_profesor_institucion'),
    ]

    operations = [
        migrations.AddField(
            model_name='profesor',
            name='carrera',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='carrera.carrera'),
        ),
    ]