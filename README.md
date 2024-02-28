# Prédiction des Emissions de CO2 des Véhicules Commercialisés en France

## Contexte: 

Depuis 2001, l’ADEME(Agence de l'Environnement et de la Maîtrise de l'Energie) acquiert tous les ans des données sur les émissions de polluants et les caractéristiques techniques des véhicules commercialisés en France auprès de l’Union Technique de l’Automobile du motocycle et du Cycle UTAC (en charge de l’homologation des véhicules avant leur mise en vente) en accord avec le ministère du développement durable.

Pour chaque véhicule, les données d’origine (transmises par l’Utac) sont les suivantes :

. les consommations de carburant

. les émissions de dioxyde de carbone (CO2)

. les émissions des polluants de l’air (réglementés dans le cadre de la norme Euro)

. l’ensemble des caractéristiques techniques des véhicules (gammes, marques, modèles, n° de CNIT, type   d’énergie ...)

## Objectif

L'objectif de ce projet est de prédire les émissions de dioxyde de carbonne (CO2) des véhicules commercialisés en France en utilisant comme informations leurs caractéristiques techniques et leurs consommations en carburant. Différentes méthodes d'apprentissage automatique (**Régression Linéaire**, **RandomForest**, **XGBoost**) sont utilisés. Après une comparaison des performances de chacune d'elles, le meilleur modèle est choisi et déployé via l'API(Application Programming Interface) **FastAPI** et via un interface graphique web **Streamlit**. Cette interface web va permettre de rendre exploitable notre modèle par un utilisateur lambda qui pourra faire des prédictions en utilisant de nouvelles informations provennants de nouveaux véhicules. Notre application web est déployé sur un serveur distant.

Le projet comporte trois fichiers de code. Le fichier Prediction_Notebook.ipynb représente le code de modélisation des données, le fichier FastAPI.py est le code de déploiement du meilleur modèle via **FastAPI** et le fichier streamlit.py est le code de déploiement du meilleur modèle sur une application **streamlit**. 

La base de données que nous avons exploité est celle de l'année 2015 et est fournis par le site gouvernemental data.gouv.fr.

Source des données: https://www.data.gouv.fr/fr/datasets/emissions-de-co2-et-de-polluants-des-vehicules-commercialises-en-france/


## Méthodologie

Après une importation du jeu de données,j'éffectue une **analyse exploratoire** qui consiste à éffectuer les **statistiques descriptives** ainsi qu'une recherche des **corrélations** existantes entre les variables. La **modélisation** des données est ensuite appréhender et le meilleur modèle est choisis et sauvégarder pour être déployé. Le meilleur modèle de prédiction de CO2 est ensuite mise en production à travers FastAPI et intègré également dans une application Streamlit pour permettre aux utilisateurs d'interagir avec le modèle et de faire des prédictions en saisisant en paramètres les données du véhicule dont ils souhaitent prédire l'émission de CO2.

## Résultats

A l'issue de notre étude, nous somme parvenus aux résultats suivants:

<u>*Statistiques descriptives:*</u>

- Les trois marques de véhicules les plus polluantes en 2015 sont les véhicules de marque LAMBORGHINI suivies de ceux de marques ROOLS-ROYS et ASTON-MARTIN.

- Les véhicules de haute gamme et de moyenne gamme polluent plus que les véhicules de gamme inférieure ou économique.

<u>*Modélisation:*</u>

- Le meilleur modèle d'apprentissage automatique pour la prédiction des émissions de co2 est le modèle XGBoost(eXtreme Gradient Boosting) qui offre de meilleures performances que les Régression linéaire et le RandomForest.

- La variable consommation extra urbaine de carburant (en l/100km) est celle qui a le plus d'influence sur la prédiction de l'emission de CO2. 

<u>*Déploiement:*</u>

Le modèle XGBoost(eXtreme Gradient Boosting) a été déployé et est exploitable via le [lien](https://prediction-emissions-co2-france.streamlit.app/)

