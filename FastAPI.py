import pandas as pd
from joblib import load
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import uvicorn


# Chargement des données (cette ligne peut être retirée)
df = pd.read_csv('data.csv', sep=';', decimal=',', encoding='ISO-8859-1')

# Chargement du modèle
best_model = load('bestModel.joblib')

# Création d'une nouvelle instance FastAPI
app = FastAPI()

# Définission d'une classe pour les requêtes
class RequestBody(BaseModel):
    puissance_administrative: float
    consommation_extra_urbaine_de_carburant_en_litre_sur_100km: float
    masse_en_ordre_de_marche_minimale_en_kg: float
    masse_en_ordre_de_marche_maximale_en_kg: float

# Définition de l'endpoint de prédiction
@app.post("/predict")  
async def predict(data: RequestBody):

    # Préparation des données pour la prédiction
    new_data = [[
        data.puissance_administrative,
        data.consommation_extra_urbaine_de_carburant_en_litre_sur_100km,
        data.masse_en_ordre_de_marche_minimale_en_kg,
        data.masse_en_ordre_de_marche_maximale_en_kg
    ]]

    colonnes=['puiss_admin_98', 'conso_mixte', 'masse_ordma_min', 'masse_ordma_max']
    new_data=pd.DataFrame(new_data,columns=colonnes)

    # Prédiction
    prediction = best_model.predict(new_data)

    prediction = prediction.tolist()  
    return JSONResponse(content={"Prédiction de CO2": prediction})

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)