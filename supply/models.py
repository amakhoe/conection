from django.db import models

escolhas = [
    ('M', 'Motos'),
    ('C', 'Carro')
]

class order(models.Model):
    criado_por = models.DateField(auto_now_add=True)

class produtos(models.Model):
    breferencia = models.IntegerField()
    bproduto = models.CharField(max_length=40)
    bquantidade = models.IntegerField()
    biva = models.IntegerField()



class categoria(models.Model):
    bcate = models.CharField(max_length=35)

class marcas(models.Model):
    bmarcas = models.CharField(max_length=35)
    bescol = models.CharField(max_length=35, choices=escolhas)

class fornecedor(models.Model):
    fempresa = models.CharField(max_length=35)
    fendereco = models.CharField(max_length=40)
    femail = models.EmailField()
    fcelular = models.IntegerField()

