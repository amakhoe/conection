from django.contrib import admin
from .models import fornecedor, order, produtos
# Register your models here.

admin.site.register(fornecedor)
admin.site.register(produtos)
admin.site.register(order)
