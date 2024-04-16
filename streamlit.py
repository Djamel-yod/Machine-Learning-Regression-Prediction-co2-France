import streamlit as st
import pandas as pd
from joblib import load

# Chargement des données (Facultatif)
#df = pd.read_csv('data.csv', sep=';', decimal=',', encoding='ISO-8859-1')

# Chargement du modèle
best_model = load('bestModel.joblib')


# Titre de l'application
st.title('Prédiction des émissions de CO2 en France')
st.subheader('Auteur: Ismael YODA')
st.write("Cette application est destinée à éffectuer la prédiction en g/km des émissions de CO2 des véhicules commercialisés en France. Elle prend en entrée les caractéristiques techniques du véhicule et sa consommation en carburant et elle renvoie en sortie la prédiction de son émission de CO2 en g/km.")


# Fonction de prédiction
def predict_CO2(puissance_administrative, consommation_extra_urbaine_de_carburant, masse_en_ordre_de_marche_minimale, masse_en_ordre_de_marche_maximale):
    new_data = [[
        puissance_administrative,
        consommation_extra_urbaine_de_carburant,
        masse_en_ordre_de_marche_minimale,
        masse_en_ordre_de_marche_maximale
    ]]

    colonnes=['puiss_admin_98', 'conso_mixte', 'masse_ordma_min', 'masse_ordma_max']
    new_data = pd.DataFrame(new_data, columns=colonnes)

    prediction = best_model.predict(new_data)
    return prediction

# Formulaire pour saisir les données d'entrée
puissance_administrative = st.number_input('Puissance administrative du véhicule')
consommation_extra_urbaine_de_carburant = st.number_input('Consommation extra-urbaine de carburant (en litres/100km)')
masse_en_ordre_de_marche_minimale = st.number_input('Masse en ordre de marche minimale (en kg)')
masse_en_ordre_de_marche_maximale = st.number_input('Masse en ordre de marche maximale (en kg)')

# Bouton pour effectuer la prédiction
if st.button('Prédire'):
    prediction = predict_CO2(puissance_administrative, consommation_extra_urbaine_de_carburant, masse_en_ordre_de_marche_minimale, masse_en_ordre_de_marche_maximale)
    st.success(f'Prédiction de CO2 en g/km: {prediction[0]}')
