# Generated by Django 4.1.4 on 2023-03-13 01:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminusers_app', '0003_alter_user_managers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='email address'),
        ),
    ]
