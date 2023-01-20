import pandas as pd

# Cette fonction retourne un dataFrame qui contient les X numéros les + sortis avec ou pas le nombre de fois où ils sont sortis
def least_numbers(dataFrameNumeros, nbrNumber=5, occurence=False):
    # Tri des lignes du dataFrame par occurrences en ordre croissant
    dataFrameNumeros.sort_values(by='occurrences', ascending=True, inplace=True)

    # Sélection des "nbrNumber" premières lignes (les X numéros les moins fréquents)
    least_numbers = dataFrameNumeros.head(nbrNumber)

    # Si on veut un dataFrame sans les occurences
    if(occurence==False):
        # On retourne un dataFrame qui contient les X numéros les - sortis
        return least_numbers.index.values

    # Si on veut un dataFrame avec les occurences
    else:
        # On retourne un dataFrame qui contient les X numéros les - sortis avec le nombre de fois où ils sont sortis
        return least_numbers

# Cette fonction retourne un dataFrame qui contient les X numérosChance les - sortis avec ou pas le nombre de fois où ils sont sortis
def least_numbersChance(dataFrameNumerosChance, nbrNumberChance=1, occurence=False):
    # Tri des lignes du dataFrame par occurrences en ordre croissant
    dataFrameNumerosChance.sort_values(by='occurrences', ascending=True, inplace=True)

    # Sélection des "nbrNumberChance" premières lignes (les X numérosChance les moins fréquents)
    least_numerosChance = dataFrameNumerosChance.head(nbrNumberChance)

    # Si on veut un dataFrame sans les occurences
    if(occurence==False):
        # On retourne un dataFrame qui contient les X numérosChance les - sortis
        return least_numerosChance.index.values

    # Si on veut un dataFrame avec les occurences
    else:
        # On retourne un dataFrame qui contient les X numérosChance les - sortis avec le nombre de fois où ils sont sortis
        return least_numerosChance