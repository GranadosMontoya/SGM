# Generated by Django 4.1.4 on 2023-01-31 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminusers_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(blank=True, choices=[('Masculino', 'Masculino'), ('Femenino', 'Femenino')], max_length=10),
        ),
    ]
