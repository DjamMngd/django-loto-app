from django.shortcuts import render
from .loto_logic import main as mainLoto

# Create your views here.

def index(request):
    return render(request, 'loto/index.html')

def about(request): 
    return render(request, 'loto/about.html')

def contact(request):
    return render(request, 'loto/contact.html')

def generate_loto_numbers(request):
    
    # On appelle la fonction top_numbers du fichier main de la partie logique afin d'obtenir les 5 numéros les plus joués
    return render(request, 'loto/generate_numbers.html', {'top_numbers' : mainLoto.top_numbers(mainLoto.dataFrameOccurrencesNumeros,5,False), 
    'top_numbersChance' : mainLoto.top_numbers(mainLoto.dataFrameOccurrencesNumerosChance,1,False), 'random_tirage_loto' : mainLoto.get_random_tirage_loto()})



