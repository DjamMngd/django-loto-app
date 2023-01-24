import pandas as pd
import os
from loto.settings import BASE_DIR

def mergingCSV():

    #print("*** Merging multiple csv files into a single pandas dataframe ***")

    if os.name == "nt":
        # Mes 4 fichiers CSV de data du loto (Windows)
        data_loto_oct2008_mar2017 = "tirages\loto_logic\Historique\loto - De octobre 2008 à mars 2017 - cleared.csv"
        data_loto_mar2017_fev2019 = "tirages\loto_logic\Historique\loto - De mars 2017 à février 2019 - cleared.csv"
        data_loto_fev2019_nov2019 = "tirages\loto_logic\Historique\loto - De février 2019 à novembre 2019 - cleared.csv"
        data_loto_nov2019_now = "tirages\loto_logic\Historique\loto - Depuis novembre 2019 - cleared.csv"

        # Mon fichier CSV Final à creer (Windows):
        file_data_Loto_Final = "tirages\loto_logic\Historique\loto - Final.csv"
    else:
        # Mes 4 fichiers CSV de data du loto (Linux)
        data_loto_oct2008_mar2017 = "tirages/loto_logic/Historique/loto - De octobre 2008 à mars 2017 - cleared.csv"
        data_loto_mar2017_fev2019 = "tirages/loto_logic/Historique/loto - De mars 2017 à février 2019 - cleared.csv"
        data_loto_fev2019_nov2019 = "tirages/loto_logic/Historique/loto - De février 2019 à novembre 2019 - cleared.csv"
        data_loto_nov2019_now = "tirages/loto_logic/Historique/loto - Depuis novembre 2019 - cleared.csv"

        # Mon fichier CSV Final à creer (Linux):
        file_data_Loto_Final = "tirages/loto_logic/Historique/loto - Final.csv"
    
    # merge files
    data_Loto_Final = pd.concat(map(pd.read_csv, [data_loto_oct2008_mar2017, data_loto_mar2017_fev2019, data_loto_fev2019_nov2019, data_loto_nov2019_now]), ignore_index=True)

    # convertir la colonne de dates en format datetime
    data_Loto_Final['date_de_tirage'] = pd.to_datetime(data_Loto_Final['date_de_tirage'], format="%d/%m/%Y")

    # trier les lignes en fonction de la colonne de dates
    data_Loto_Final = data_Loto_Final.sort_values(by='date_de_tirage', ascending=True)

    # On crée un fichier CSV Final avec toutes les grilles reunies (ça peut toujours servir)
    data_Loto_Final.to_csv(file_data_Loto_Final, index=False)

    return data_Loto_Final