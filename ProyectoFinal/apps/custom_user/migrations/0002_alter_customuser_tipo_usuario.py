# Generated by Django 4.2.6 on 2023-11-12 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custom_user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='tipo_usuario',
            field=models.CharField(blank=True, choices=[('Alumno', 'Alumno'), ('Institución', 'Institución'), ('Profesor', 'Profesor')], default='Alumno', max_length=20, null=True),
        ),
    ]
