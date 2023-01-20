import random

def get_random_number(nbrNumbers = 5):
    # Cette fonction permet de générer plusieurs nombres aléatoires unique
    random_numbers = random.sample(range(1, 50), nbrNumbers)

    return random_numbers

def get_random_numberChance(nbrNumbersChance = 1):
    # Cette fonction permet de générer plusieurs nombres aléatoires unique
    random_numbersChance = random.sample(range(1, 11), nbrNumbersChance)

    return random_numbersChance

def get_random_tirage_loto(nbrTirages = 1):

    # On initialise une liste pour notre tirage
    tirageLoto = []

    # On met dans notre liste les 5 numéros au hasard
    tirageLoto = get_random_number()

    # On y ajoute le numéro chance à la fin
    tirageLoto.append(get_random_numberChance())

    # On retoune ce tirage
    return tirageLoto