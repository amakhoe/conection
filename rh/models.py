from django.db import models

# Classe RH
class Recursos_Humanos(models.Model):
    bnome = models.CharField(max_length=35)
    bcelular = models.IntegerField()
    btelefone = models.IntegerField()
    bfax = models.CharField(max_length=15)
    bemail = models.CharField(max_length=29)
    bmorada = models.CharField(max_length=29)
    blocalidade = models.CharField(max_length=29)
    bzona = models.CharField(max_length=20)
    bpais = models.CharField(max_length=20)
    bnuit = models.CharField(max_length=35, unique=True)
    bobserv = models.TextField()
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.bnome
