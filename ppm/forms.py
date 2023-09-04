from django import forms
from .models import *
class ActiviteForm(forms.ModelForm):
    class Meta:
        model = Activite
        fields = '__all__'
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'prix': forms.NumberInput(attrs={'class': 'form-control'}),
            'age_minimum': forms.NumberInput(attrs={'class': 'form-control'}),
            'capacite_max': forms.NumberInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'nom': 'Nom de l\'activité',
            'description': 'Description de l\'activité',
            'prix': 'Prix de l\'activité',
            'age_minimum': 'Âge minimum requis',
            'capacite_max': 'Capacité maximale',
        }

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = '__all__'
        widgets = {
            'activite': forms.Select(attrs={'class': 'form-control'}),
            'date_reservation': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'date_activite': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'nom_client': forms.TextInput(attrs={'class': 'form-control'}),
            'email_client': forms.EmailInput(attrs={'class': 'form-control'}),
            'telephone_client': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre_participants': forms.NumberInput(attrs={'class': 'form-control'}),
            'statut': forms.Select(attrs={'class': 'form-control'}),
        }
        labels = {
            'activite': 'Activité',
            'date_reservation': 'Date de réservation',
            'date_activite': 'Date de l\'activité',
            'nom_client': 'Nom du client',
            'email_client': 'Adresse e-mail du client',
            'telephone_client': 'Numéro de téléphone du client',
            'nombre_participants': 'Nombre de participants',
            'statut': 'Statut',
        }

class EmployeForm(forms.ModelForm):
    class Meta:
        model = Employe
        fields = '__all__'
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control'}),
            'statut': forms.Select(attrs={'class': 'form-control'}),
            'email_employee': forms.EmailInput(attrs={'class': 'form-control'}),
            'telephone': forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'nom': 'Nom de l\'employé',
            'statut': 'Statut de l\'employé',
            'email_employee': 'Adresse e-mail de l\'employé',
            'telephone': 'Numéro de téléphone de l\'employé',
        }

class PaiementForm(forms.ModelForm):
    class Meta:
        model = Paiement
        fields = '__all__'
        widgets = {
            'type_paiement': forms.TextInput(attrs={'class': 'form-control'}),
            'montant': forms.NumberInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'type_paiement': 'Type de paiement',
            'montant': 'Montant du tarif',
        }

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'sujet': forms.TextInput(attrs={'class': 'form-control'}),
            'message': forms.Textarea(attrs={'class': 'form-control'}),
        }
        labels = {
            'nom': 'Votre nom',
            'email': 'Votre adresse e-mail',
            'sujet': 'Sujet du message',
            'message': 'Message',
        }

class StatistiqueForm(forms.ModelForm):
    class Meta:
        model = Statistique
        fields = '__all__'
        widgets = {
            'activite': forms.Select(attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'participants': forms.NumberInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'activite': 'Activité',
            'date': 'Date',
            'participants': 'Nombre de participants',
        }

class RapportForm(forms.ModelForm):
    class Meta:
        model = Rapport
        fields = '__all__'
        widgets = {
            'activite': forms.Select(attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'contenu': forms.Textarea(attrs={'class': 'form-control'}),
        }
        labels = {
            'activite': 'Activité',
            'date': 'Date',
            'contenu': 'Contenu du rapport',
        }

class EquipementForm(forms.ModelForm):
    class Meta:
        model = Equipement
        fields = '__all__'
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'date_achat': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'prix': forms.NumberInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'nom': 'Nom de l\'équipement',
            'description': 'Description de l\'équipement',
            'date_achat': 'Date d\'achat',
            'prix': 'Prix de l\'équipement',
        }

class TarifForm(forms.ModelForm):
    class Meta:
        model = Activite
        fields = ['nom', 'prix']


