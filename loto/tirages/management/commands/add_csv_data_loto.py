import os
from django.core.management.base import BaseCommand
import pandas as pd
from datetime import datetime
from tirages.models import Loto

class Command(BaseCommand):
    #help = 'Load data from a CSV file into the Loto model'

    def handle(self, *args, **options):
        # Ici on ajoute toutes les nouvelles grilles du loto dans la base de donnée
        data = pd.read_csv(os.path.join("tirages", "loto_logic", "Historique", "loto - Add data.csv"))
        for i, row in data.iterrows():
            date_de_tirage = datetime.strptime(row['date_de_tirage'], '%d/%m/%Y')
            combinaison_gagnante = row['combinaison_gagnante_en_ordre_croissant']
            boule_1 = row['boule_1']
            boule_2 = row['boule_2']
            boule_3 = row['boule_3']
            boule_4 = row['boule_4']
            boule_5 = row['boule_5']
            numero_chance = row['numero_chance']
            loto = Loto(date_de_tirage=date_de_tirage, combinaison_gagnante_en_ordre_croissant=combinaison_gagnante, boule_1=boule_1, boule_2=boule_2, boule_3=boule_3, boule_4=boule_4, boule_5=boule_5, numero_chance=numero_chance)
            loto.save()
