import pandas as pd
from .merging_csv import mergingCSV
from .calcul_occurences import calculOccurrences
from .top_numbers import top_numbers, top_numbersChance
from .least_numbers import least_numbers, least_numbersChance
from .random_numbers import get_random_number, get_random_numberChance, get_random_tirage_loto

# On merge notre fichier loto dans un seul et on récupère le dataFrame de tous les numéros
data_Loto_Final = mergingCSV()

# On va creer nos fichiers qui contiendront les occurrences des numeros normaux et des numeros chance
dataFrameOccurrencesNumeros, dataFrameOccurrencesNumerosChance = calculOccurrences(data_Loto_Final)

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



