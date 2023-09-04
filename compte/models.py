from django.contrib.auth.models import AbstractUser
from django.db import models

class Administrateur(AbstractUser):
    photo_de_profil = models.ImageField(upload_to='profil/', blank=True, null=True)
    mon_champ = models.CharField(max_length=100)

    def __str__(self):
        return self.username
