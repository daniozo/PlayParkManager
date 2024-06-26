from django.contrib import admin
from .models import Activite, Reservation, Employe, Paiement, Contact, Rapport, Statistique

class ActiviteAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prix', 'age_minimum', 'capacite_max')
    list_filter = ('nom',)
    search_fields = ('nom', 'description')

class ReservationAdmin(admin.ModelAdmin):
    list_display = ('nom_client', 'activite', 'date_activite', 'statut')
    list_filter = ('statut',)
    search_fields = ('nom_client', 'email_client')

class EmployeAdmin(admin.ModelAdmin):
    list_display = ('nom', 'statut')
    list_filter = ('statut',)
    search_fields = ('nom',)

class PaiementAdmin(admin.ModelAdmin):
    list_display = ('activite', 'type_paiement', 'montant')
    list_filter = ('activite',)
    search_fields = ('type_paiement',)

class ContactAdmin(admin.ModelAdmin):
    list_display = ('nom', 'email', 'sujet')
    search_fields = ('nom', 'email', 'sujet')

class RapportAdmin(admin.ModelAdmin):
    list_display = ('activite', 'date')
    list_filter = ('activite',)
    search_fields = ('activite__nom',)

class StatistiqueAdmin(admin.ModelAdmin):
    list_display = ('activite', 'date', 'participants')
    list_filter = ('date',)
    search_fields = ('activite__nom',)

admin.site.register(Activite, ActiviteAdmin)
admin.site.register(Reservation, ReservationAdmin)
admin.site.register(Employe, EmployeAdmin)
admin.site.register(Paiement, PaiementAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Rapport, RapportAdmin)
admin.site.register(Statistique, StatistiqueAdmin)
