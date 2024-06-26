# Generated by Django 4.2 on 2023-08-17 13:50

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ppm', '0002_contact_employe_alter_activite_image_tarif_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Statistique',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.date.today)),
                ('participants', models.PositiveIntegerField()),
                ('activite', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ppm.activite')),
            ],
        ),
        migrations.CreateModel(
            name='Rapport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.date.today)),
                ('contenu', models.TextField()),
                ('activite', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ppm.activite')),
            ],
        ),
    ]
