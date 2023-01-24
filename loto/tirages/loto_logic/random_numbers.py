import random

# Partie random du Loto

def get_random_loto_number(nbrNumbers = 5):
    # Cette fonction permet de générer plusieurs nombres aléatoires unique
    random_numbers = random.sample(range(1, 50), nbrNumbers)

    return random_numbers

def get_random_loto_numberChance(nbrNumbersChance = 1):
    # Cette fonction permet de générer plusieurs nombres aléatoires unique
    random_numbersChance = random.sample(range(1, 11), nbrNumbersChance)

    return random_numbersChance

def get_random_tirage_loto(nbrTirages = 1):

    # On initialise une liste pour notre tirage
    tirageLoto = []

    # On met dans notre liste les 5 numéros au hasard
    tirageLoto = get_random_loto_number()

    # On initialise une liste pour les étoiles
    numeroChanceLoto = []

    # On lance le tirage des 2 étoiles
    numeroChanceLoto = get_random_loto_numberChance()

    # On y ajoute le numéro chance à la fin
    tirageLoto.append(numeroChanceLoto[0])

    # On retoune ce tirage
    return tirageLoto

# Partie random de l'EuroMillion

def get_random_euroMillion_number(nbrNumbers = 5):
    # Cette fonction permet de générer plusieurs nombres aléatoires unique
    random_numbers = random.sample(range(1, 51), nbrNumbers)

    return random_numbers

def get_random_euroMillion_numberChance(nbrNumbersChance = 2):
    # Cette fonction permet de générer plusieurs nombres aléatoires unique
    random_numbersChance = random.sample(range(1, 13), nbrNumbersChance)

    return random_numbersChance

def get_random_tirage_euroMillion(nbrTirages = 1):

    # On initialise une liste pour notre tirage
    tirageEuroMillion = []

    # On met dans notre liste les 5 numéros au hasard
    tirageEuroMillion = get_random_euroMillion_number()

    # On initialise une liste pour les étoiles
    etoilesEuroMillion = []

    # On lance le tirage des 2 étoiles
    etoilesEuroMillion = get_random_euroMillion_numberChance(2)

    # On y ajoute les 2 numéros chance à la fin
    tirageEuroMillion.append(etoilesEuroMillion[0])    
    tirageEuroMillion.append(etoilesEuroMillion[1])

    # On retoune ce tirage
    return tirageEuroMillion


# Creer une fonction qui sort des chiffres aléatoires mais qui 
# une fois le chiffre sorti roll un tirage d'un / (le nombre de fois où ce numeros est sorti) et si ce roll est on le chiffre est validé
# Il se peut que cette fonction soit très très longue en exécution au vu de l'aleatoire possible pour les tirages
# mais à test car ca peut être drôle

# Essayer de voir aussi si chatGPT voir une suite logique dans les sorties de grilles du Loto