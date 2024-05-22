import streamlit as st
import pandas as pd
import plotly.express as px
from bs4 import BeautifulSoup
import requests
import re
import df_call


# ---------------------------
# Paramètre de la page

# Modifying the page title and icon
st.set_page_config(page_title = "Le Senechal - Movie Reco", page_icon = ":clapper:", layout = "wide")

# CSS code to make the width of columns match with lenght of text
st.markdown("""
            <style>
                div[data-testid="column"] {
                    width: fit-content !important;
                    flex: unset;
                }
                div[data-testid="column"] * {
                    width: fit-content !important;
                }
                [data-testid="stSidebarNav"]::before {
                content: "Navigation";
                margin-left: 20px;
                margin-top: 20px;
                font-size: 30px;
                position: relative;
                color: orange;
                font-family: Source Sans Pro, sans_serif;
                top: 100px;
                }
            </style>
            """, unsafe_allow_html=True)


movie = df_call.df_final()

st.markdown("<h1 style='text-align: center; color: orange;'>Le Sénéchal<br>-<br>Recherche & recommandation de films</h1>", unsafe_allow_html=True)

st.header("Bienvenue", divider = "orange")

# ---------------------------
# Thème de la semaine

st.subheader("En avant cette semaine, notre planète si bleue")
st.subheader("Planet Ocean")
st.image("https://image.tmdb.org/t/p/w500/" + movie["poster_path"][movie["originalTitle"].str.contains("planet ocean", case = False)].iloc[0])


st.write("Synopsis:")
movie["overview"][movie["originalTitle"].str.contains("planet ocean", case = False)].iloc[0]

# ---------------------------
# Vote pour la diffusion d'un film

st.header("Vous pouvez ici voter pour la diffusion de cette semaine", divider = "orange")
st.write("Cochez un ou plusieurs films")

with st.form("Vote"):
    film1 = st.checkbox("Film 1")
    film2 = st.checkbox("Film 2")
    film3 = st.checkbox("Film 3")
    
    selection = {"Film 1": film1,
                 "Film 2": film2,
                 "Film 3": film3}
    vote = st.form_submit_button("Film à diffuser")
    
    if vote:
        for key, val in selection.items():
            if val == 1:
                st.write(f"Vous avez voté pour {key}")

# ---------------------------
# Partie Infos Pratiques

st.header("Infos Pratiques", divider = "orange")
# Web Scrapping du site 
SéanceURL = "https://www.cinema-senechal.com/horaires/"
EventURL = "https://www.cinema-senechal.com/tous-nos-evenements/"

pageSéance = requests.get(SéanceURL)
pageEvent = requests.get(EventURL)
soupSéance = BeautifulSoup(pageSéance.text, "html.parser")
soupEvent = BeautifulSoup(pageEvent.text, "html.parser")

# Donner des informations sur la prochaine séance
# st.subheader("Prochaine séance:")
# st.write("Web scrap du site?")

# Donner des informations sur le prochain évènement
st.subheader("Prochain évènement:")
col1, col2 = st.columns([0.4, 0.6])
event_image = soupEvent.find("img", {"class": "css-b5to1a"})
col1.image(event_image["src"])
event = soupEvent.find("div", {"class": "css-194pin2"})
col2.write(event.find("h2", {"class": "css-zkq0cp"}).text)
date = re.findall("(\w+) (\d+) (\w+) (\d+)", event.text)[0]
col2.write("Ce " + date[0] + " " + date[1] + " " + date[2] + " " + date[3])

st.subheader("Les tarifs")
st.dataframe(pd.DataFrame({"Catégorie": ["- de 14 ans", 
                                         "Jeune (- de 18 ans)",
                                         "Etudiant",
                                         "Demandeur d'emploi - famille nombreuse",
                                         "Senior (+ de 60 ans)",
                                         "Tarif dimanche matin",
                                         "Normal",
                                         "Abonnement 5 places valable 6 mois",
                                         "Abonnement 10 places valable 1 an"],
                           "Prix": ["5,00 €",
                                    "7,30 €",
                                    "7,30 €",
                                    "7,30 €",
                                    "7,30 €",
                                    "6,00 €",
                                    "8,80 €",
                                    "32,50 €",
                                    "65,00 €"]}), hide_index = True)

st.subheader("Pour plus d'infos ou pour réserver, rendez-vous [ici](https://www.cinema-senechal.com/)")
          