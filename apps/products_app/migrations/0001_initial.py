# Generated by Django 4.1.4 on 2023-03-10 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('code', models.IntegerField(unique=True)),
                ('amount', models.IntegerField()),
                ('entry_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('exit_price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]