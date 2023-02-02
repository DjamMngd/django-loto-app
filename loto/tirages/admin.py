from django.contrib import admin
from tirages.models import Loto, EuroMillion, OccurrencesNumerosLoto, OccurrencesNumerosChanceLoto, OccurrencesNumerosEuroMillion, OccurrencesNumerosChanceEuroMillion

# Register your models here.

class LotoAdmin(admin.ModelAdmin):
    list_display = ('date_de_tirage', 'combinaison_gagnante_en_ordre_croissant', 'boule_1', 'boule_2', 'boule_3', 'boule_4', 'boule_5', 'numero_chance')

class EuroMillionAdmin(admin.ModelAdmin):
    list_display = ('date_de_tirage', 'boules_gagnantes_en_ordre_croissant', 'etoiles_gagnantes_en_ordre_croissant', 'boule_1', 'boule_2', 'boule_3', 'boule_4', 'boule_5', 'numero_chance_1', 'numero_chance_2')

class OccurrencesNumerosLotoAdmin(admin.ModelAdmin):
    list_display = ('numero', 'occurrences')

class OccurrencesNumerosChanceLotoAdmin(admin.ModelAdmin):
    list_display = ('numero_chance', 'occurrences')

class OccurrencesNumerosEuroMillionAdmin(admin.ModelAdmin):
    list_display = ('numero', 'occurrences')

class OccurrencesNumerosChanceEuroMillionAdmin(admin.ModelAdmin):
    list_display = ('numero_chance', 'occurrences')

admin.site.register(Loto, LotoAdmin)
admin.site.register(EuroMillion, EuroMillionAdmin)
admin.site.register(OccurrencesNumerosLoto, OccurrencesNumerosLotoAdmin)
admin.site.register(OccurrencesNumerosChanceLoto, OccurrencesNumerosChanceLotoAdmin)
admin.site.register(OccurrencesNumerosEuroMillion, OccurrencesNumerosEuroMillionAdmin)
admin.site.register(OccurrencesNumerosChanceEuroMillion, OccurrencesNumerosChanceEuroMillionAdmin)
