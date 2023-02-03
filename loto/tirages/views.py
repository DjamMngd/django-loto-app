from django.shortcuts import render
from .loto_logic import main_database as mainLoto
from datetime import datetime
from django.http import JsonResponse
from tirages.models import Loto, EuroMillion
from tirages.forms import ContactUsForm
from django.core.mail import send_mail
from django.shortcuts import redirect

# Create your views here.

def index(request):
    loto = Loto.objects.latest('date_de_tirage')
    euroMillion = EuroMillion.objects.latest('date_de_tirage')
    current_year = datetime.now()
    return render(request, 'loto/index.html', {'year': current_year, 'loto': loto, 'euroMillion': euroMillion})

def about(request): 
    current_year = datetime.now()
    return render(request, 'loto/about.html', {'year': current_year})

def contact(request):
    current_year = datetime.now()

    # ajoutez ces instructions d'impression afin que nous puissions jeter un coup d'oeil à « request.method » et à « request.POST »
    # print('La méthode de requête est : ', request.method)
    # print('Les données POST sont : ', request.POST)
    
    if request.method == 'POST':
        # créer une instance de notre formulaire et le remplir avec les données POST
        form = ContactUsForm(request.POST)
        if form.is_valid():
            send_mail(
            subject=f'Message de {form.cleaned_data["name"] or "anonyme"} par le formulaire de contact de Bons Numéros',
            message=form.cleaned_data['message'],
            from_email=form.cleaned_data['email'],
            recipient_list=['admin@tirages.xyz'],
        )
        return redirect('email_sent')  # ajoutez cette instruction de retour
    # si le formulaire n'est pas valide, nous laissons l'exécution continuer jusqu'au return
    # ci-dessous et afficher à nouveau le formulaire (avec des erreurs).
    else:
    # ceci doit être une requête GET, donc créer un formulaire vide
        form = ContactUsForm()  # ajout d’un nouveau formulaire ici

    
    return render(request, 'loto/contact.html', {'year': current_year, 'form' : form})

def email_sent(request):
    return render(request, 'loto/email_sent.html')

def generate_loto_numbers(request):
    current_year = datetime.now()
    # On appelle la fonction Python qui sorte les numéros dont j'ai besoin
    #print("trage loto : ", mainLoto.get_random_tirage_loto())
    return render(
        request, 
        'loto/generate_loto_numbers.html', 
        {
            'top_numbers_loto' : mainLoto.top_numbers(mainLoto.dataFrameOccurrencesNumerosLoto,5,False), 
            'top_numbersChance_loto' : mainLoto.top_numbers(mainLoto.dataFrameOccurrencesNumerosChanceLoto,1,False), 
            'least_numbers_loto' : mainLoto.least_numbers(mainLoto.dataFrameOccurrencesNumerosLoto,5,False), 
            'least_numbersChance_loto' : mainLoto.least_numbers(mainLoto.dataFrameOccurrencesNumerosChanceLoto,1,False),
            'random_tirage_loto' : mainLoto.get_random_tirage_loto(), 
            'year': current_year
        }
    )

def generate_euroMillion_numbers(request):
    current_year = datetime.now()
    # On appelle la fonction Python qui sorte les numéros dont j'ai besoin
    #print("tirage euroMillion : ", mainLoto.get_random_tirage_euroMillion())
    return render(
        request, 
        'loto/generate_euroMillion_numbers.html', 
        {
            'top_numbers_euroMillion' : mainLoto.top_numbers(mainLoto.dataFrameOccurrencesNumerosEuroMillion,5,False), 
            'top_numbersChance_euroMillion' : mainLoto.top_numbers(mainLoto.dataFrameOccurrencesNumerosChanceEuroMillion,2,False), 
            'least_numbers_euroMillion' : mainLoto.least_numbers(mainLoto.dataFrameOccurrencesNumerosEuroMillion,5,False), 
            'least_numbersChance_euroMillion' : mainLoto.least_numbers(mainLoto.dataFrameOccurrencesNumerosChanceEuroMillion,2,False),
            'random_tirage_euroMillion' : mainLoto.get_random_tirage_euroMillion(),
            'year': current_year
        }
    )

def newRandomLotoNumbers(request):
    random_tirage_loto = mainLoto.get_random_tirage_loto()
    return JsonResponse({'random_tirage_loto': random_tirage_loto})


def newRandomEuroMillionNumbers(request):
    random_tirage_euroMillion = mainLoto.get_random_tirage_euroMillion()
    return JsonResponse({'random_tirage_euroMillion': random_tirage_euroMillion})

def stats_loto(request):
    if request.method == 'POST':
        if request.POST.get('submit_button') == 'Numeros':
            df_stats_loto_ordonne = mainLoto.dataFrameOccurrencesNumerosLoto.sort_values(by='numero')
        else:
            df_stats_loto_ordonne = mainLoto.dataFrameOccurrencesNumerosChanceLoto
            df_stats_loto_ordonne.rename(columns={'numero_chance': 'numero'}, inplace=True)
            df_stats_loto_ordonne = df_stats_loto_ordonne.sort_values(by='numero')
    else:
        df_stats_loto_ordonne = mainLoto.dataFrameOccurrencesNumerosLoto.sort_values(by='numero')
    
    return render(request, 'loto/stats_loto.html', {'stats' : df_stats_loto_ordonne})

def stats_euroMillion(request):
    if request.method == 'POST':
        if request.POST.get('submit_button') == 'Numeros':
            df_stats_euroMillion_ordonne = mainLoto.dataFrameOccurrencesNumerosEuroMillion.sort_values(by='numero')
        else:
            df_stats_euroMillion_ordonne = mainLoto.dataFrameOccurrencesNumerosChanceEuroMillion
            df_stats_euroMillion_ordonne.rename(columns={'numero_chance': 'numero'}, inplace=True)
            df_stats_euroMillion_ordonne = df_stats_euroMillion_ordonne.sort_values(by='numero')
    else:
        df_stats_euroMillion_ordonne = mainLoto.dataFrameOccurrencesNumerosEuroMillion.sort_values(by='numero')
    
    return render(request, 'loto/stats_euroMillion.html', {'stats' : df_stats_euroMillion_ordonne})