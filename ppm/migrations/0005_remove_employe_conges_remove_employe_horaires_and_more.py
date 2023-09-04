# Generated by Django 4.2 on 2023-08-21 01:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ppm', '0004_remove_activite_choix_activite'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employe',
            name='conges',
        ),
        migrations.RemoveField(
            model_name='employe',
            name='horaires',
        ),
        migrations.AddField(
            model_name='employe',
            name='email_employee',
            field=models.EmailField(default='example@example.com', max_length=254),
        ),
        migrations.AddField(
            model_name='employe',
            name='telephone',
            field=models.CharField(default='+212060000000', max_length=20),
        ),
    ]
