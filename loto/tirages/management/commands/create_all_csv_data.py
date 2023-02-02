from tirages.loto_logic.merging_csv import mergingCSV, mergingCSV_euroMillion
from tirages.loto_logic.calcul_occurences import calculOccurrences, calculOccurrences_EuroMillion

# ------------------------ A NE FAIRE QU'UNE FOIS ------------------------- #
# On merge nos fichiers loto dans un seul (même chose avec l'euroMillion)
data_Loto_Final = mergingCSV()
data_EuroMillion_Final = mergingCSV_euroMillion()

# On va creer nos fichiers qui contiendront les occurrences des numeros normaux et des numeros chance
# dataFrameOccurrencesNumerosLoto, dataFrameOccurrencesNumerosChanceLoto = calculOccurrences(data_Loto_Final)
calculOccurrences(data_Loto_Final)

# On va creer nos fichiers qui contiendront les occurrences des numeros normaux et des numeros chance
# dataFrameOccurrencesNumerosEuroMillion, dataFrameOccurrencesNumerosChanceEuroMillion = calculOccurrences_EuroMillion(data_EuroMillion_Final)
calculOccurrences_EuroMillion(data_EuroMillion_Final)