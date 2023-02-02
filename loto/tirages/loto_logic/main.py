import os
import pandas as pd
from .merging_csv import mergingCSV, mergingCSV_euroMillion
from .calcul_occurences import calculOccurrences, calculOccurrences_EuroMillion
from .top_numbers import top_numbers, top_numbersChance
from .least_numbers import least_numbers, least_numbersChance
from .random_numbers import get_random_loto_number, get_random_loto_numberChance, get_random_tirage_loto
from .random_numbers import get_random_euroMillion_number, get_random_euroMillion_numberChance, get_random_tirage_euroMillion

# # ------------------------ A NE FAIRE QU'UNE FOIS ------------------------- #
# # On merge nos fichiers loto dans un seul (même chose avec l'euroMillion)
# data_Loto_Final = mergingCSV()
# data_EuroMillion_Final = mergingCSV_euroMillion()

# # On va creer nos fichiers qui contiendront les occurrences des numeros normaux et des numeros chance
# dataFrameOccurrencesNumerosLoto, dataFrameOccurrencesNumerosChanceLoto = calculOccurrences(data_Loto_Final)

# # On va creer nos fichiers qui contiendront les occurrences des numeros normaux et des numeros chance
# dataFrameOccurrencesNumerosEuroMillion, dataFrameOccurrencesNumerosChanceEuroMillion = calculOccurrences_EuroMillion(data_EuroMillion_Final)

print("Le main est exécuté")

'''
# --------------------- ANCIENNE VERSION CAR ON NE JOUE PLUS AVEC LES FICHIERS CSV MAIS DIRECTEMENT AVEC LA BDD --------------------- #

# On va creer nos fichiers qui contiendront les occurrences des numeros normaux et des numeros chance
dataFrameOccurrencesNumerosLoto, dataFrameOccurrencesNumerosChanceLoto = calculOccurrences(data_Loto_Final)

# On va creer nos fichiers qui contiendront les occurrences des numeros normaux et des numeros chance
dataFrameOccurrencesNumerosEuroMillion, dataFrameOccurrencesNumerosChanceEuroMillion = calculOccurrences_EuroMillion(data_EuroMillion_Final)

# On récupére les 5 numéros les plus joués avec ou sans leurs occurences (True = avec, False = sans)
print(top_numbers(dataFrameOccurrencesNumeros,5,False))

# On récupère le ou les étoiles les plus jouées avec ou sans leurs occurences (True = avec, False = sans)
print(top_numbersChance(dataFrameOccurrencesNumerosChance,1,False))

# On récupére les 5 numéros les moins joués
print(least_numbers(dataFrameOccurrencesNumeros))

# On récupère le ou les étoiles les moins jouées
print(least_numbersChance(dataFrameOccurrencesNumerosChance))

# On génére 5 numéros aleatoires
print(get_random_number())

# On génére un numéro chance aleatoire
print(get_random_numberChance())

# On génére une grille du loto aléatoire
print(get_random_tirage_loto())

'''

