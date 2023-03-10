import pandas as pd
import os

def calculOccurrences(data_Loto_Final):

    # Plus besoin de se soucier du système d'exploitation avec os.path.join :
    file_dataFrameOccurrencesNumeros = os.path.join("tirages", "loto_logic", "Historique", "loto - Occurences Numeros.csv")
    file_dataFrameOccurrencesNumerosChance = os.path.join("tirages", "loto_logic", "Historique", "loto - Occurences Numero Chance.csv")

    # On va creer un dictionnaire qui contiendra le nombre de fois où chaque numéro est sorti
    nbrOccurrenceNumeros = {}

    # On va check pour chaque numéro combien de fois il est sorti
    for cpt in range(1,50):
        nbrOccurrenceNumeros[str(cpt)] = (data_Loto_Final[['boule_1', 'boule_2', 'boule_3', 'boule_4', 'boule_5']] == cpt).sum().sum()


    # On va creer un dictionnaire qui contiendra le nombre de fois où chaque étoiles est sortie
    nbrOccurrenceNumeroChance = {}

    # On va check pour chaque numéro combien de fois il est sorti
    for cpt in range(1,11):
        nbrOccurrenceNumeroChance[str(cpt)] = (data_Loto_Final[['numero_chance']] == cpt).sum().sum()


    # On va tester de creer le dataFrame directement avec le nombre de fois où les numéros sont sortis :

    # On le fait d'abord avec les numéros de base

    # Creating a DataFrame from dictionary
    dataFrameOccurrencesNumeros = pd.DataFrame.from_dict(nbrOccurrenceNumeros, orient='index', columns=['value'])

    # Renaming column
    dataFrameOccurrencesNumeros = dataFrameOccurrencesNumeros.rename(columns={'value': 'occurrences'})
    dataFrameOccurrencesNumeros = dataFrameOccurrencesNumeros.rename_axis("numero", axis='columns')

    # On crée un fichier CSV qui contient le dataFrame du nombre d'occurences pour chaque numéros.
    dataFrameOccurrencesNumeros.to_csv(file_dataFrameOccurrencesNumeros, index_label='numero', header='occurrences')

    # Puis avec le numéro chance

    # Creating a DataFrame from dictionary
    dataFrameOccurrencesNumerosChance = pd.DataFrame.from_dict(nbrOccurrenceNumeroChance, orient='index', columns=['value'])

    # Renaming column
    dataFrameOccurrencesNumerosChance = dataFrameOccurrencesNumerosChance.rename(columns={'value': 'occurrences'})
    dataFrameOccurrencesNumerosChance = dataFrameOccurrencesNumerosChance.rename_axis("numero_chance", axis='columns')

    # On crée un fichier CSV qui contient le dataFrame du nombre d'occurences pour chaque numéros.
    dataFrameOccurrencesNumerosChance.to_csv(file_dataFrameOccurrencesNumerosChance, index_label='numero_chance', header='occurrences')

    return dataFrameOccurrencesNumeros, dataFrameOccurrencesNumerosChance

def calculOccurrences_EuroMillion(data_EuroMillion_Final):

    # Plus besoin de se soucier du système d'exploitation avec os.path.join :
    file_dataFrameOccurrencesNumeros = os.path.join("tirages", "loto_logic", "Historique", "euroMillion - Occurences Numeros.csv")
    file_dataFrameOccurrencesNumerosChance = os.path.join("tirages", "loto_logic", "Historique", "euroMillion - Occurences Numero Chance.csv")

    # On va creer un dictionnaire qui contiendra le nombre de fois où chaque numéro est sorti
    nbrOccurrenceNumeros = {}

    # On va check pour chaque numéro combien de fois il est sorti
    for cpt in range(1,51):
        nbrOccurrenceNumeros[str(cpt)] = (data_EuroMillion_Final[['boule_1', 'boule_2', 'boule_3', 'boule_4', 'boule_5']] == cpt).sum().sum()


    # On va creer un dictionnaire qui contiendra le nombre de fois où chaque étoiles est sortie
    nbrOccurrenceNumeroChance = {}

    # On va check pour chaque numéro combien de fois il est sorti
    for cpt in range(1,13):
        nbrOccurrenceNumeroChance[str(cpt)] = (data_EuroMillion_Final[['numero_chance_1','numero_chance_2']] == cpt).sum().sum()


    # On va tester de creer le dataFrame directement avec le nombre de fois où les numéros sont sortis :

    # On le fait d'abord avec les numéros de base

    # Creating a DataFrame from dictionary
    dataFrameOccurrencesNumeros = pd.DataFrame.from_dict(nbrOccurrenceNumeros, orient='index', columns=['value'])

    # Renaming column
    dataFrameOccurrencesNumeros = dataFrameOccurrencesNumeros.rename(columns={'value': 'occurrences'})
    dataFrameOccurrencesNumeros = dataFrameOccurrencesNumeros.rename_axis("numero", axis='columns')

    # On crée un fichier CSV qui contient le dataFrame du nombre d'occurences pour chaque numéros.
    dataFrameOccurrencesNumeros.to_csv(file_dataFrameOccurrencesNumeros, index_label='numero', header='occurrences')

    # Puis avec le numéro chance

    # Creating a DataFrame from dictionary
    dataFrameOccurrencesNumerosChance = pd.DataFrame.from_dict(nbrOccurrenceNumeroChance, orient='index', columns=['value'])

    # Renaming column
    dataFrameOccurrencesNumerosChance = dataFrameOccurrencesNumerosChance.rename(columns={'value': 'occurrences'})
    dataFrameOccurrencesNumerosChance = dataFrameOccurrencesNumerosChance.rename_axis("numero_chance", axis='columns')

    # On crée un fichier CSV qui contient le dataFrame du nombre d'occurences pour chaque numéros.
    dataFrameOccurrencesNumerosChance.to_csv(file_dataFrameOccurrencesNumerosChance, index_label='numero_chance', header='occurrences')

    return dataFrameOccurrencesNumeros, dataFrameOccurrencesNumerosChance
