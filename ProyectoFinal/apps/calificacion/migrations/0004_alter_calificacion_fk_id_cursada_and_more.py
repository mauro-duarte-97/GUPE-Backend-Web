# Generated by Django 4.2.6 on 2023-11-10 23:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cursada', '0003_cursada_titulo'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('calificacion', '0003_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calificacion',
            name='fk_id_cursada',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='calificacion', to='cursada.cursada'),
        ),
        migrations.AlterField(
            model_name='calificacion',
            name='fk_id_usuario',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='calificacion', to=settings.AUTH_USER_MODEL),
        ),
    ]