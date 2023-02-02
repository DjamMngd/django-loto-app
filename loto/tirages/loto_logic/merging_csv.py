import os
import pandas as pd

def mergingCSV():

    #print("*** Merging multiple csv files into a single pandas dataframe ***")

    # Plus besoin de se soucier du système d'exploitation avec os.path.join :
    data_loto_oct2008_mar2017 = os.path.join("tirages", "loto_logic", "Historique", "loto - De octobre 2008 à mars 2017 - cleared.csv")
    data_loto_mar2017_fev2019 = os.path.join("tirages", "loto_logic", "Historique", "loto - De mars 2017 à février 2019 - cleared.csv")
    data_loto_fev2019_nov2019 = os.path.join( "tirages", "loto_logic", "Historique", "loto - De février 2019 à novembre 2019 - cleared.csv")
    data_loto_nov2019_now = os.path.join("tirages", "loto_logic", "Historique", "loto - Depuis novembre 2019 - cleared.csv")

    # Mon fichier CSV Final à creer (Windows):
    file_data_Loto_Final = os.path.join("tirages", "loto_logic", "Historique", "loto - Final.csv")
    
    # merge files
    data_Loto_Final = pd.concat(map(pd.read_csv, [data_loto_oct2008_mar2017, data_loto_mar2017_fev2019, data_loto_fev2019_nov2019, data_loto_nov2019_now]), ignore_index=True)

    # convertir la colonne de dates en format datetime
    data_Loto_Final['date_de_tirage'] = pd.to_datetime(data_Loto_Final['date_de_tirage'], format="%d/%m/%Y")

    # trier les lignes en fonction de la colonne de dates
    data_Loto_Final = data_Loto_Final.sort_values(by='date_de_tirage', ascending=True)

    # On crée un fichier CSV Final avec toutes les grilles reunies (ça peut toujours servir)
    data_Loto_Final.to_csv(file_data_Loto_Final, index=False)

    return data_Loto_Final

def mergingCSV_euroMillion():

    #print("*** Merging multiple csv files into a single pandas dataframe ***")

    # Plus besoin de se soucier du système d'exploitation avec os.path.join :
    data_euroMillion_sep2016_fev2019 = os.path.join( "tirages", "loto_logic", "Historique", "euroMillion - De septembre 2016 à février 2019 - cleared.csv")
    data_leuroMillion_fev2019_fev2020 = os.path.join("tirages", "loto_logic", "Historique", "euroMillion - De février 2019 à février 2020 - cleared.csv")
    data_euroMillion_fev2020_now = os.path.join("tirages", "loto_logic", "Historique", "euroMillion - Depuis février 2020 - cleared.csv")

    # Mon fichier CSV Final à creer (Windows):
    file_data_euroMillion_Final = os.path.join("tirages", "loto_logic", "Historique", "euroMillion - Final.csv")

    # merge files
    data_EuroMillion_Final = pd.concat(map(pd.read_csv, [data_euroMillion_sep2016_fev2019, data_leuroMillion_fev2019_fev2020, data_euroMillion_fev2020_now]), ignore_index=True)

    # convertir la colonne de dates en format datetime
    data_EuroMillion_Final['date_de_tirage'] = pd.to_datetime(data_EuroMillion_Final['date_de_tirage'], format="%d/%m/%Y")

    # trier les lignes en fonction de la colonne de dates
    data_EuroMillion_Final = data_EuroMillion_Final.sort_values(by='date_de_tirage', ascending=True)

    # On va renommer les colonnes etoile_1 et etoile_2 en numero_chance_1 et numero_chance_2 pour réutiliser plus facilement le code du Loto
    data_EuroMillion_Final.rename(columns={'etoile_1': 'numero_chance_1'}, inplace=True)
    data_EuroMillion_Final.rename(columns={'etoile_2': 'numero_chance_2'}, inplace=True)

    # On crée un fichier CSV Final avec toutes les grilles reunies (ça peut toujours servir)
    data_EuroMillion_Final.to_csv(file_data_euroMillion_Final, index=False)

    return data_EuroMillion_Final