import os
from django.core.management.base import BaseCommand
import pandas as pd
from datetime import datetime
from tirages.models import Loto, OccurrencesNumerosLoto, OccurrencesNumerosChanceLoto

class Command(BaseCommand):
    help = 'Load data from a CSV file into the Loto model'

    #def add_arguments(self, parser):
    #    parser.add_argument('csv_file', type=str, help='tirages/loto_logic/Historique/loto - Final.csv')

    def handle(self, *args, **options):
        # Ici on ajoute rentre toutes les grilles du Loto dans la base de donnée

        data = pd.read_csv(os.path.join("tirages", "loto_logic", "Historique", "loto - Final.csv"))
        for i, row in data.iterrows():
            date_de_tirage = datetime.strptime(row['date_de_tirage'], '%Y-%m-%d')
            combinaison_gagnante = row['combinaison_gagnante_en_ordre_croissant']
            boule_1 = row['boule_1']
            boule_2 = row['boule_2']
            boule_3 = row['boule_3']
            boule_4 = row['boule_4']
            boule_5 = row['boule_5']
            numero_chance = row['numero_chance']
            loto = Loto(date_de_tirage=date_de_tirage, combinaison_gagnante_en_ordre_croissant=combinaison_gagnante, boule_1=boule_1, boule_2=boule_2, boule_3=boule_3, boule_4=boule_4, boule_5=boule_5, numero_chance=numero_chance)
            loto.save()

        # Ici on ajoute rentre toutes les occurende du Loto dans la base de donnée
        data = pd.read_csv(os.path.join("tirages", "loto_logic", "Historique", "loto - Occurences Numeros.csv"))
        for i, row in data.iterrows():
            numero = row['numero']
            occurrences = row['occurrences']
            occurrencesNumerosLoto = OccurrencesNumerosLoto(
                numero=numero, 
                occurrences=occurrences)
            occurrencesNumerosLoto.save()
        
        # Ici on ajoute rentre toutes les occurences du Loto dans la base de donnée
        data = pd.read_csv(os.path.join("tirages", "loto_logic", "Historique", "loto - Occurences Numero Chance.csv"))
        for i, row in data.iterrows():
            numero_chance = row['numero_chance']
            occurrences = row['occurrences']
            occurrencesNumerosChanceLoto = OccurrencesNumerosChanceLoto(
                numero_chance=numero_chance, 
                occurrences=occurrences)
            occurrencesNumerosChanceLoto.save()