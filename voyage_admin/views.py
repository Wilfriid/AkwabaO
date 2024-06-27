from django.shortcuts import render , redirect
import pandas as pd
import pickle
from django.contrib.auth.forms import UserCreationForm 
from .forms import CustomUserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Charger le modèle entraîné
with open('C:\\Users\\SIMPLON\\akwabao\\recommandations\\recommendation_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Charger le dataset
data = pd.read_csv('C:\\Users\\SIMPLON\\akwabao\\recommandations\\destinations.csv')

def acceuil(request, *args, **kwargs):
    return render(request, 'index.html')

@login_required(login_url='connexion')
@login_required
def destination(request):
    return render(request, 'destination.html')


@login_required(login_url='connexion')
def offres(request):
    return render(request, 'offres.html')

def contact(request):
    return render(request, 'contact.html')
def propos(request):
    return render(request, 'propos.html')

@login_required(login_url='connexion')
def abidjan(request):
    return render(request, 'abidjan.html')

@login_required(login_url='connexion')
def recommendation(request):
    if request.method == 'POST':
        budget_jour = float(request.POST.get('budget_jour'))
        duree_sejour = int(request.POST.get('duree_sejour'))
        preferences_voyage = request.POST.get('preferences_voyage').capitalize()
        activites_voyage = request.POST.get('activites_voyage').capitalize()
        hotel_etoiles = request.POST.get('hotel_etoiles').strip()

        # Préparer les features pour la recommandation
        if hotel_etoiles == "Hotel 3*":
            hotel_field = 'Hotel 3*'
        elif hotel_etoiles == "Hotel 4*":
            hotel_field = 'Hotel 4*'
        elif hotel_etoiles == "Hotel 5*":
            hotel_field = 'Hotel 5*'
        else:
            hotel_field = None

        if hotel_field:
            input_features = [[budget_jour, duree_sejour, 0, 0, 0]]
            if hotel_field == 'Hotel 3*':
                input_features[0][2] = budget_jour
            elif hotel_field == 'Hotel 4*':
                input_features[0][3] = budget_jour
            elif hotel_field == 'Hotel 5*':
                input_features[0][4] = budget_jour

            distances, indices = model.kneighbors(input_features)

            recommendations = []
            for index in indices[0]:
                recommendation = data.iloc[index]
                recommendations.append({
                    'Pays': recommendation["Pays"],
                    'Budget': recommendation["Budget Moy./Jour (EUR)"],
                    'Duree': recommendation["Duree Moy. (jours)"],
                    'Preferences': recommendation["Preferences"],
                    'Activites': recommendation["Activites"],
                    'Hotel_3': recommendation["Hotel 3*"],
                    'Hotel_4': recommendation["Hotel 4*"],
                    'Hotel_5': recommendation["Hotel 5*"],
                })

            return render(request, 'results.html', {'recommendations': recommendations, 'hotel_etoiles': hotel_etoiles})

    return render(request, 'home.html')




# Create your views here.
def inscription(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('connexion')
    else:
        form = CustomUserCreationForm()
    return render(request, 'inscription.html', {'form': form})

def connexion(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('destination')
        else:
            messages.error(request, 'Nom d\'utilisateur ou mot de passe incorrect.')
    return render(request, 'connexion.html')



def deconnexion(request):
    logout(request)
    return redirect('connexion')


# graphique
# Importations nécessaires
# Importations nécessaires
# Importations nécessaires
# Importations nécessaires
# Importations nécessaires
# Importations nécessaires
import pandas as pd
import plotly.graph_objs as go
from django.shortcuts import render
from io import StringIO

def statistique(request):
    # Lire le fichier CSV
    csv_data = """
    Pays,Visiteurs_annuels,Cout,Categorie
    Maroc,12300000,Moyen,Moyen
    Afrique du Sud,10000000,Cher,Plus cher
    Tunisie,8700000,Moyen,Moyen
    Algerie,2600000,Moyen,Moyen
    Seychelles,1950000,Abordable,Moins cher
    Zimbabwe,2500000,Abordable,Moins cher
    Kenya,2000000,Abordable,Moins cher
    Cote d'ivoire,2400000,Abordable,Moins cher
    Turquie,1500000,Cher,Plus cher
    Comorres,1200000,Cher,Plus cher
    Cap Vert,1000000,Abordable,Plus cher
    Madagascar,1800000,Moyen,Moyen
    Senegal,1500000,Abordable,Moins cher
    Ghana,1200000,Abordable,Moins cher
    Egypte,11700000,Abordable,Moins cher
    Angola,1700000,Abordable,Moins cher
    """

    # Charger les données dans un DataFrame pandas
    df = pd.read_csv(StringIO(csv_data))

    # Supprimer les espaces autour des noms de colonnes (au cas où)
    df.columns = df.columns.str.strip()

    # Trier les données pour obtenir les 5 pays les plus visités
    top_5_visites = df.nlargest(5, 'Visiteurs_annuels')

    # Filtrer les données par catégorie de coût
    df_cher = df[df['Categorie'] == 'Plus cher']
    df_moyen = df[df['Categorie'] == 'Moyen']
    df_abordable = df[df['Categorie'] == 'Moins cher']

    # Créer des graphiques avec Plotly

    # Graphique des 5 pays les plus visités (bar chart)
    fig1 = go.Figure()
    fig1.add_trace(go.Bar(
        x=top_5_visites['Pays'],
        y=top_5_visites['Visiteurs_annuels'],
        name='Top 5 des pays les plus visités',
        marker_color='rgb(255, 165, 0)'
    ))
    fig1.update_layout(
        title='Top 5 des pays les plus visités',
        xaxis_title='Pays',
        yaxis_title='Visiteurs annuels',
        barmode='group'
    )

    # Graphique des pays les plus chers (line chart)
    fig2 = go.Figure()
    fig2.add_trace(go.Scatter(
        x=df_cher['Pays'],
        y=df_cher['Visiteurs_annuels'],
        mode='lines+markers',
        name='Pays les plus chers',
        line=dict(color='rgb(255, 0, 0)')
    ))
    fig2.update_layout(
        title='Pays les plus chers',
        xaxis_title='Pays',
        yaxis_title='Visiteurs annuels'
    )

    # Graphique des pays de coût moyen (pie chart)
    fig3 = go.Figure()
    fig3.add_trace(go.Pie(
        labels=df_moyen['Pays'],
        values=df_moyen['Visiteurs_annuels'],
        name='Pays de coût moyen'
    ))
    fig3.update_layout(
        title='Pays de coût moyen'
    )

    # Graphique des pays les moins chers (scatter plot)
    fig4 = go.Figure()
    fig4.add_trace(go.Scatter(
        x=df_abordable['Pays'],
        y=df_abordable['Visiteurs_annuels'],
        mode='markers',
        name='Pays les moins chers',
        marker=dict(size=15, color='rgb(0, 0, 255)')
    ))
    fig4.update_layout(
        title='Pays les moins chers',
        xaxis_title='Pays',
        yaxis_title='Visiteurs annuels'
    )

    # Convertir les graphiques en HTML pour être rendu dans un template Django
    graph1_html = fig1.to_html(full_html=False)
    graph2_html = fig2.to_html(full_html=False)
    graph3_html = fig3.to_html(full_html=False)
    graph4_html = fig4.to_html(full_html=False)

    # Rendre le template avec les graphiques
    return render(request, 'statistique.html', {
        'graph1': graph1_html,
        'graph2': graph2_html,
        'graph3': graph3_html,
        'graph4': graph4_html,
    })
