import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_card import card
import df_call

# Modifying the page title and icon
st.set_page_config(page_title = "Le Senechal - Genre", page_icon = ":tv:", layout = "wide")

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
                div[data-testid="column"] {
                    margin-right: 5px;
                    margin-left: 5px;
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

st.markdown("<h1 style='text-align: center; color: orange;'>Rechercher par genre</h1>", unsafe_allow_html=True)
st.header("Vous pouvez effectuer votre recherche ci-dessous", divider = "orange")

genre_search = st.text_input("Genre:", value="")

# Filter the dataframe using masks
try:
    m1 = movie["genres_x"].str.contains(genre_search, case = False)
    search = movie[m1].sort_values("popularity", ascending = False)
except:
    st.error("Nous n'avons malheureusement trouvé aucun film correspondant à votre recherche")

searching_list = []
# Show the results, if you have a text_search
if genre_search:
    
    col1, col2, col3, col4, col5, col6, col7, col8, col9, col10, col11, col12, col13, col14, col15, col16 = st.columns(16)
    col = [col1, col2, col3, col4, col5, col6, col7, col8, col9, col10, col11, col12, col13, col14, col15, col16]

    
    for ind, numCol in enumerate(col):
        try:
            with numCol:
                card_one = card(title = search["title_x"][search["genres_x"] == search["genres_x"].iloc[ind]].iloc[0],
                                text = search["overview"][search["genres_x"] == search["genres_x"].iloc[ind]].iloc[0],
                                image = "https://image.tmdb.org/t/p/w500" + search["poster_path"][search["genres_x"] == search["genres_x"].iloc[ind]].iloc[0],
                                styles = {"card" :{"width": "200",
                                                    "height": "400px",
                                                    "border_radius": "60px"},
                                        "text": {"font_family": "calibri"},
                                        "title": {"font_family": "cambria"}})
        except:
            with numCol:
                st.write("")
