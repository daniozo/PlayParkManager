# Generated by Django 4.2 on 2023-09-01 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ppm', '0006_equipement'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rapport',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='statistique',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
