from django.contrib.auth.views import LogoutView
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.db.models import Count, Sum


@login_required(login_url='compte:compte')
def dashboard(request):
    reservations = Reservation.objects.all()
    activites = Activite.objects.all()
    activites_plus_reservees = Activite.objects.annotate(num_reservations=Count('reservation')).order_by(
        '-activite_id')[ :5 ]

    statistiques = Statistique.objects.values('date').annotate(participants=Sum('participants')).order_by('date')

    context = {
        'activites_plus_reservees': activites_plus_reservees,
        'statistiques': statistiques,
        'reservations':reservations,
        'activites':activites,
    }

    return render(request, 'admin/dashboard.html', context)

@login_required(login_url='compte:compte')
def index(request):
    return render(request, 'admin/index.html')

@login_required(login_url='compte:compte')
def gestion_activites(request):
    activites = Activite.objects.all()
    form = ActiviteForm()  # Créez une instance du formulaire ActiviteForm

    if request.method == 'POST':
        if 'modifier' in request.POST:
            activite_id = request.POST['activite_id']
            nouveau_nom = request.POST['nouveau_nom']
            nouvelle_description = request.POST['nouvelle_description']
            nouveau_prix =float(request.POST['nouveau_prix'].replace(',', '.'))
            nouvel_age_minimum = float(request.POST['nouvel_age_minimum'])
            nouvelle_capacite_max = float(request.POST['nouvelle_capacite_max'])
            activite = Activite.objects.get(pk=activite_id)
            activite.nom = nouveau_nom
            activite.description = nouvelle_description
            activite.prix = nouveau_prix
            activite.age_minimum = nouvel_age_minimum
            activite.capacite_max = nouvelle_capacite_max
            activite.save()
        elif 'supprimer' in request.POST:
            activite_id = request.POST['activite_id']
            activite = Activite.objects.get(pk=activite_id)
            activite.delete()
        elif 'ajouter' in request.POST:
            form = ActiviteForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('ppm:gestion_activites')

    context = {'activites': activites, 'form': form}
    return render(request, 'admin/gest_act.html', context)



@login_required(login_url='compte:compte')
def gestion_reservations(request):
    reservations = Reservation.objects.all()
    activites = Activite.objects.all()

    if request.method == 'POST':
        if 'modifier' in request.POST:
            reservation_id = request.POST['reservation_id']
            nouvelle_date_activite = request.POST['nouvelle_date_activite']
            nouveau_nom_client = request.POST['nouveau_nom_client']
            nouvel_email_client = request.POST['nouvel_email_client']
            nouveau_telephone_client = request.POST['nouveau_telephone_client']
            nouveau_nombre_participants = request.POST['nouveau_nombre_participants']
            nouveau_statut = request.POST['statut']
            reservation = Reservation.objects.get(pk=reservation_id)
            reservation.date_activite = nouvelle_date_activite
            reservation.nom_client = nouveau_nom_client
            reservation.email_client = nouvel_email_client
            reservation.telephone_client = nouveau_telephone_client
            reservation.nombre_participants = nouveau_nombre_participants
            reservation.statut = nouveau_statut
            reservation.save()
        elif 'supprimer' in request.POST:
            reservation_id = request.POST['reservation_id']
            reservation = Reservation.objects.get(pk=reservation_id)
            reservation.delete()
        elif 'ajouter' in request.POST:
            activite_id = request.POST['activite']
            date_activite = request.POST['date_activite']
            nom_client = request.POST['nom_client']
            email_client = request.POST['email_client']
            telephone_client = request.POST['telephone_client']
            nombre_participants = request.POST['nombre_participants']
            statut = request.POST['statut']
            activite = Activite.objects.get(pk=activite_id)
            nouvelle_reservation = Reservation(
                activite=activite,
                date_activite=date_activite,
                nom_client=nom_client,
                email_client=email_client,
                telephone_client=telephone_client,
                nombre_participants=nombre_participants,
                statut=statut
            )
            nouvelle_reservation.save()

    context = {'reservations': reservations, 'activites': activites}
    return render(request, 'admin/gest_res.html', context)



@login_required(login_url='compte:compte')
def gestion_personnel(request):
        employes = Employe.objects.all()
        form = EmployeForm()

        if request.method == 'POST':
            form = EmployeForm(request.POST)
            if 'modifier' in request.POST:
                employe_id = request.POST[ 'employe_id' ]
                employe = Employe.objects.get(pk=employe_id)
                form = EmployeForm(request.POST, instance=employe)
                if form.is_valid():
                    form.save()
            elif 'supprimer' in request.POST:
                employe_id = request.POST[ 'employe_id' ]
                employe = Employe.objects.get(pk=employe_id)
                employe.delete()
            elif 'ajouter' in request.POST:
                if form.is_valid():
                    form.save()
                    return redirect('ppm:gestion_personnel')

        context = {'employes': employes, 'form': form}
        return render(request, 'admin/gest_pers.html', context)


@login_required(login_url='compte:compte')
def gestion_tarifs(request):
    # Récupérez la liste des activités avec leurs tarifs actuels
    activites = Activite.objects.all()
    paiements = Paiement.objects.all()

    # Récupérez la liste des types de paiement
    types_paiement = Paiement.TYPE_PAIEMENT_CHOICES

    # Initialisez les formulaires
    tarif_form = TarifForm()
    paiement_form = PaiementForm()

    if request.method == 'POST':
        # Si le formulaire pour modifier les tarifs est soumis
        if 'modifier_tarifs' in request.POST:
            tarif_form = TarifForm(request.POST)
            if tarif_form.is_valid():
                tarif_form.save()
                return redirect('ppm:gestion_tarifs')

        # Si le formulaire pour ajouter un paiement est soumis
        elif 'ajouter_paiement' in request.POST:
            paiement_form = PaiementForm(request.POST)
            if paiement_form.is_valid():
                paiement_form.save()
                return redirect('ppm:gestion_tarifs')

    context = {
        'activites': activites,
        'paiements': paiements,
        'types_paiement': types_paiement,
        'tarif_form': tarif_form,
        'paiement_form': paiement_form,
    }

    return render(request, 'admin/gest_tarif.html', context)


@login_required(login_url='compte:compte')
def gestion_rapports(request):
    statistiques = Statistique.objects.all()
    form = StatistiqueForm()

    if request.method == 'POST':
        form = StatistiqueForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ppm:gestion_rapports')

    context = {'statistiques': statistiques, 'form': form}
    return render(request, 'admin/gest_rapp.html', context)





@login_required(login_url='compte:compte')
def reservations_precedentes(request):
    reservations = Reservation.objects.all()
    context = {'reservations_precedentes': reservations}  # Utilisez la variable 'reservations' ici
    return render(request, 'admin/reservations_precedentes.html', context)


@login_required(login_url='compte:compte')
def gestion_contacts(request):
    contacts = Contact.objects.all()

    if request.method == 'POST':
        if 'supprimer' in request.POST:
            contact_id = request.POST['contact_id']
            contact = Contact.objects.get(pk=contact_id)
            contact.delete()
        elif 'ajouter' in request.POST:
            nouveau_nom = request.POST['nouveau_nom']
            nouvel_email = request.POST['nouvel_email']
            nouveau_sujet = request.POST['nouveau_sujet']
            nouveau_message = request.POST['nouveau_message']
            nouveau_contact = Contact(
                nom=nouveau_nom,
                email=nouvel_email,
                sujet=nouveau_sujet,
                message=nouveau_message
            )
            nouveau_contact.save()
            return redirect('ppm:gestion_contacts')  # Rediriger vers la page après l'ajout
        elif 'modifier' in request.POST:
            contact_id = request.POST['contact_id']
            contact = Contact.objects.get(pk=contact_id)
            contact.nom = request.POST['nouveau_nom']
            contact.email = request.POST['nouvel_email']
            contact.sujet = request.POST['nouveau_sujet']
            contact.message = request.POST['nouveau_message']
            contact.save()

    context = {'contacts': contacts}
    return render(request, 'admin/contact.html', context)



@login_required(login_url='compte:compte')
def gestion_stats_rapports(request):
    statistiques = Statistique.objects.all()
    rapports = Rapport.objects.all()
    statistique_form = StatistiqueForm()
    rapport_form = RapportForm()

    if request.method == 'POST':
        if 'ajouter_statistique' in request.POST:
            statistique_form = StatistiqueForm(request.POST)
            if statistique_form.is_valid():
                statistique_form.save()
        elif 'ajouter_rapport' in request.POST:
            rapport_form = RapportForm(request.POST)
            if rapport_form.is_valid():
                rapport_form.save()
        elif 'modifier_statistique' in request.POST:
            statistique_id = request.POST['statistique_id']
            statistique = Statistique.objects.get(pk=statistique_id)
            statistique_form = StatistiqueForm(request.POST, instance=statistique)
            if statistique_form.is_valid():
                statistique_form.save()
        elif 'supprimer_statistique' in request.POST:
            statistique_id = request.POST['statistique_id']
            statistique = Statistique.objects.get(pk=statistique_id)
            statistique.delete()
        elif 'modifier_rapport' in request.POST:
            rapport_id = request.POST['rapport_id']
            rapport = Rapport.objects.get(pk=rapport_id)
            rapport_form = RapportForm(request.POST, instance=rapport)
            if rapport_form.is_valid():
                rapport_form.save()
        elif 'supprimer_rapport' in request.POST:
            rapport_id = request.POST['rapport_id']
            rapport = Rapport.objects.get(pk=rapport_id)
            rapport.delete()

    context = {
        'statistiques': statistiques,
        'rapports': rapports,
        'statistique_form': statistique_form,
        'rapport_form': rapport_form,
    }
    return render(request, 'admin/gest_rapp.html', context)




@login_required(login_url='compte:compte')
def gestion_equipements(request):
    equipements = Equipement.objects.all()

    if request.method == 'POST':
        if 'supprimer' in request.POST:
            equipement_id = request.POST['equipement_id']
            equipement = Equipement.objects.get(pk=equipement_id)
            equipement.delete()
        elif 'ajouter' in request.POST:
            nouveau_nom = request.POST['nouveau_nom']
            nouvelle_description = request.POST['nouvelle_description']
            nouvelle_date_achat = request.POST['nouvelle_date_achat']
            nouveau_prix = request.POST['nouveau_prix']
            nouveau_equipement = Equipement(
                nom=nouveau_nom,
                description=nouvelle_description,
                date_achat=nouvelle_date_achat,
                prix=nouveau_prix
            )
            nouveau_equipement.save()
            return redirect('gestion_equipements')
        elif 'modifier' in request.POST:
            equipement_id = request.POST['equipement_id']
            equipement = Equipement.objects.get(pk=equipement_id)
            nouveau_nom = request.POST['nouveau_nom']
            nouvelle_description = request.POST['nouvelle_description']
            nouvelle_date_achat = request.POST['nouvelle_date_achat']
            nouveau_prix = request.POST['nouveau_prix']
            equipement.nom = nouveau_nom
            equipement.description = nouvelle_description
            equipement.date_achat = nouvelle_date_achat
            equipement.prix = nouveau_prix
            equipement.save()

    context = {'equipements': equipements}
    return render(request, 'admin/gest_equip.html', context)

from django.urls import reverse_lazy

class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('compte:compte')  # Remplacez 'nom_de_votre_page_de_connexion' par le nom de la vue de connexion
