from django.db import models
import datetime
from django.contrib.auth.models import User



# Create your models here.
class Interessat(models.Model):
    user = models.ForeignKey(User, unique=True)
    telf = models.IntegerField()



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
    interessat = models.ForeignKey(Interessat)
    sala = models.ForeignKey(Salas)
    data_inici = models.DateField('Data inici')
    data_final = models.DateField('Data final')
    data_sol = models.DateTimeField(datetime.date.today())

    def demanat_avui(self):
        return self.data_sol.date() == datetime.date.today()









