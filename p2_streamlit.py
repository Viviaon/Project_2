import streamlit as st
import pandas as pd
import plotly.express as px

# Modifying the page title and icon
st.set_page_config(page_title = "Le Senechal - Movie Reco", page_icon = ":movie_camera:", layout = "wide")

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
            </style>
            """, unsafe_allow_html=True)

# link = "C:/Users/User/Wild_Code/Projects/Project_2/DB/tmdb_full.csv"
# tmdb = pd.read_csv("C:/Users/User/Wild_Code/Projects/Project_2/DB/tmdb_full.csv", sep = ",")

# tmdb[tmdb["original_title"].str.contains("star wars", case = False)]
st.title("Bienvenue sur le site du Sénéchal")
st.header("Temple de la culture cinématographique")

st.subheader("En avant cette semaine, l'un des meilleurs films de la galaxie")
st.subheader("Star Wars: A New Hope")
st.image("https://www.themoviedb.org/t/p/w600_and_h900_bestv2/6FfCtAuVAW8XJjZ7eWeLibRLWTw.jpg")
st.write("Synopsis:")
# tmdb["overview"][tmdb["original_title"].str.contains("star wars", case = False)].iloc[0]

# st.image("https://www.themoviedb.org/t/p/w600_and_h900_bestv2/6wkfovpn7Eq8dYNKaG5PY3q2oq6.jpg")

