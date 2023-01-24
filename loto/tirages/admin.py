from django.contrib import admin
from tirages.models import Loto

# Register your models here.

class LotoAdmin(admin.ModelAdmin):
    list_display = ('date_de_tirage', 'combinaison_gagnante_en_ordre_croissant', 'boule_1', 'boule_2', 'boule_3', 'boule_4', 'boule_5', 'numero_chance')

admin.site.register(Loto, LotoAdmin)
