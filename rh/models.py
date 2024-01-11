from django.db import models

# Classe RH
class Recursos_Humanos(models.Model):
    Nome = models.CharField(max_length=20)
    bi = models.IntegerField()
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Nome
    
class Gestor(models.Model):
    sector = models.CharField(max_length=20)
    roles = models.TextField()
    data = models.DateField(auto_now=True)

    def __str__(self):
        return self.sector
