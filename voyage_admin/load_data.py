# voyage_admin/load_data.py

import pandas as pd
from .models import Destination

def load_data():
    # Chemin vers votre fichier CSV
    csv_file = 'C:\\Users\\SIMPLON\\akwabao\\recommandations\\destinations.csv'
    
    # Charger les données
    data = pd.read_csv(csv_file)
    
    # Supprimer les anciennes données
    Destination.objects.all().delete()

    # Ajouter les nouvelles données
    for index, row in data.iterrows():
        Destination.objects.create(
            pays=row['Pays'],
            budget_moy_jour=row['Budget Moy./Jour (EUR)'],
            duree_moy_jours=row['Duree Moy. (jours)'],
            preferences=row['Preferences'],
            activites=row['Activites'],
            hotel_3=row['Hotel 3*'],
            hotel_4=row['Hotel 4*'],
            hotel_5=row['Hotel 5*']
        )

# Appeler la fonction pour charger les données
if __name__ == "__main__":
    load_data()
