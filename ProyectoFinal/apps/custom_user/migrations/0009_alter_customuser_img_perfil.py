# Generated by Django 5.0 on 2024-05-27 01:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custom_user', '0008_alter_customuser_nombre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='img_perfil',
            field=models.ImageField(blank=True, default='UserProfile.png', null=True, upload_to='perfiles/user_uploads/'),
        ),
    ]