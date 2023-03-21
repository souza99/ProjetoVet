from django.contrib import admin
from .models import Usuario, Cargo, Fazenda

# Register your models here.

admin.site.register(Usuario)
admin.site.register(Cargo)
admin.site.register(Fazenda)