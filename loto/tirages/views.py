from django.shortcuts import render
from .loto_logic import main as mainLoto
from datetime import datetime

# Create your views here.

def index(request):
    current_year = datetime.now()
    return render(request, 'loto/index.html', {'year': current_year})

def about(request): 
    current_year = datetime.now()
    return render(request, 'loto/about.html', {'year': current_year})

def contact(request):
    current_year = datetime.now()
    return render(request, 'loto/contact.html', {'year': current_year})

def generate_loto_numbers(request):
    current_year = datetime.now()
    # On appelle la fonction Python qui sorte les numéros dont j'ai besoin
    return render(request, 'loto/generate_numbers.html', {'top_numbers' : mainLoto.top_numbers(mainLoto.dataFrameOccurrencesNumeros,5,False), 
    'top_numbersChance' : mainLoto.top_numbers(mainLoto.dataFrameOccurrencesNumerosChance,1,False), 'least_numbers' : mainLoto.least_numbers(mainLoto.dataFrameOccurrencesNumeros,5,False), 
    'least_numbersChance' : mainLoto.least_numbers(mainLoto.dataFrameOccurrencesNumerosChance,1,False), 'random_tirage_loto' : mainLoto.get_random_tirage_loto(), 'year': current_year})



