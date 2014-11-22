from django.db import models
import datetime
from django.forms import ModelForm
from django.contrib.auth.models import User

class Tipus(models.Model):
    nom = models.CharField(max_length=200)

    def __str__(self):
        return self.nom


class Objecte(models.Model):
    nom = models.CharField(max_length=200)
    tipus = models.ForeignKey(Tipus)
    Si = 'Si'
    No = 'No'
    OPCIONS_DISPONIBLE = (
        (Si, 'Disponible'),
        (No, 'No Disponible'),
    )
    disponible = models.CharField(max_length=50, choices=OPCIONS_DISPONIBLE, default=Si)

    def __str__(self):
        return self.nom


class Salas(models.Model):
    nom = models.CharField(max_length=200)

    def __str__(self):
        return self.nom


class Reserva(models.Model):
    objecte = models.ForeignKey(Objecte)
    user = models.ForeignKey(User, unique=False)
    sala = models.ForeignKey(Salas)
    data_inici = models.DateTimeField('Data inici')
    data_final = models.DateTimeField('Data final')
    data_sol = models.DateTimeField('Data solicitud', default=datetime.datetime.now())

    def demanat_avui(self):
        return self.data_sol.date() == datetime.date.today()





