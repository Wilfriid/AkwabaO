import pandas as pd
import pickle
from sklearn.neighbors import NearestNeighbors

# Charger le dataset
data = pd.read_csv('C:\\Users\\SIMPLON\\akwabao\\recommandations\\destinations.csv')

# Préparer les fonctionnalités pour l'entraînement
features = data[['Budget Moy./Jour (EUR)', 'Duree Moy. (jours)', 'Hotel 3*', 'Hotel 4*', 'Hotel 5*']]

# Entraîner un modèle de voisin le plus proche
model = NearestNeighbors(n_neighbors=5)
model.fit(features)

# Enregistrer le modèle entraîné avec pickle
with open('recommendation_model.pkl', 'wb') as f:
    pickle.dump(model, f)

