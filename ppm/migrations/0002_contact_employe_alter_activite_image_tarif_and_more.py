# Generated by Django 4.2 on 2023-08-17 13:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ppm', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('contact_id', models.AutoField(primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('sujet', models.CharField(max_length=200)),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Employe',
            fields=[
                ('employe_id', models.AutoField(primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=100)),
                ('statut', models.CharField(choices=[('disponible', 'Disponible'), ('non_disponible', 'Non Disponible')], default='disponible', max_length=20)),
                ('horaires', models.TextField()),
                ('conges', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='activite',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='activite/'),
        ),
        migrations.CreateModel(
            name='Tarif',
            fields=[
                ('tarif_id', models.AutoField(primary_key=True, serialize=False)),
                ('type_paiement', models.CharField(max_length=100)),
                ('montant', models.DecimalField(decimal_places=2, max_digits=10)),
                ('activite', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ppm.activite')),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('reservation_id', models.AutoField(primary_key=True, serialize=False)),
                ('date_reservation', models.DateTimeField(auto_now_add=True)),
                ('date_activite', models.DateTimeField()),
                ('nom_client', models.CharField(max_length=100)),
                ('email_client', models.EmailField(max_length=254)),
                ('telephone_client', models.CharField(max_length=20)),
                ('nombre_participants', models.PositiveIntegerField()),
                ('statut', models.CharField(choices=[('en_attente', 'En Attente'), ('validee', 'Validée'), ('annulee', 'Annulée')], default='en_attente', max_length=20)),
                ('activite', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ppm.activite')),
            ],
        ),
    ]
