import os
from django.core.management.base import BaseCommand
import pandas as pd
from datetime import datetime
from tirages.models import EuroMillion

class Command(BaseCommand):
    #help = 'Load data from a CSV file into the Loto model'

    def handle(self, *args, **options):
        #csv_file = options['csv_file']
        data = pd.read_csv(os.path.join("tirages", "loto_logic", "Historique", "euroMillion - Add data.csv"))
        for i, row in data.iterrows():
            date_de_tirage = datetime.strptime(row['date_de_tirage'], '%Y-%m-%d')
            boules_gagnantes_en_ordre_croissant = row['boules_gagnantes_en_ordre_croissant']
            etoiles_gagnantes_en_ordre_croissant = row['etoiles_gagnantes_en_ordre_croissant']
            boule_1 = row['boule_1']
            boule_2 = row['boule_2']
            boule_3 = row['boule_3']
            boule_4 = row['boule_4']
            boule_5 = row['boule_5']
            numero_chance_1 = row['numero_chance_1']
            numero_chance_2 = row['numero_chance_2']
            euroMillion = EuroMillion(
                date_de_tirage=date_de_tirage, 
                boules_gagnantes_en_ordre_croissant=boules_gagnantes_en_ordre_croissant, 
                etoiles_gagnantes_en_ordre_croissant=etoiles_gagnantes_en_ordre_croissant, 
                boule_1=boule_1, boule_2=boule_2, boule_3=boule_3, boule_4=boule_4, boule_5=boule_5, 
                numero_chance_1=numero_chance_1,
                numero_chance_2=numero_chance_2)
            euroMillion.save()