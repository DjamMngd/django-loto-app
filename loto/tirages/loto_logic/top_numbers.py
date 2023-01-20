import pandas as pd

# Cette fonction retourne un dataFrame qui contient les X numéros les + sortis avec ou pas le nombre de fois où ils sont sortis
def top_numbers(dataFrameNumeros, nbrNumber=5, occurence=False):
    # Tri des lignes du dataFrame par occurrences en ordre décroissant
    dataFrameNumeros.sort_values(by='occurrences', ascending=False, inplace=True)

    # Sélection des "nbrNumber" premières lignes (les X numéros les plus fréquents)
    top_numbers = dataFrameNumeros.head(nbrNumber)

    # Si on veut un dataFrame sans les occurences
    if(occurence==False):
        # On retourne un dataFrame qui contient les X numéros les + sortis
        return top_numbers.index.values

    # Si on veut un dataFrame avec les occurences
    else:
        # On retourne un dataFrame qui contient les X numéros les + sortis avec le nombre de fois où ils sont sortis
        return top_numbers

# Cette fonction retourne un dataFrame qui contient les X numérosChance les + sortis avec ou pas le nombre de fois où ils sont sortis
def top_numbersChance(dataFrameNumerosChance, nbrNumberChance=1, occurence=False):
    # Tri des lignes du dataFrame par occurrences en ordre décroissant
    dataFrameNumerosChance.sort_values(by='occurrences', ascending=False, inplace=True)

    # Sélection des "nbrNumberChance" premières lignes (les X numérosChance les plus fréquents)
    top_numbersChance = dataFrameNumerosChance.head(nbrNumberChance)

    # Si on veut un dataFrame sans les occurences
    if(occurence==False):
        # On retourne un dataFrame qui contient les X numérosChance les + sortis
        return top_numbersChance.index.values

    # Si on veut un dataFrame avec les occurences
    else:
        # On retourne un dataFrame qui contient les X numérosChance les + sortis avec le nombre de fois où ils sont sortis
        return top_numbersChance