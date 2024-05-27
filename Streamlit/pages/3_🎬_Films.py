import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_card import card
import df_call

# Ajouter une barre de recherche 

# Modifying the page title and icon
st.set_page_config(
    page_title="Le Senechal - Movies",
    page_icon="🎥",
    layout = "wide"
)

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
                    margin-right: 1px;
                    margin-left: 1px;
                    padding: 10px;
                }
                div[class="css-5spcrp"] {
                    padding: 10px !important;
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

st.markdown("<h1 style='text-align: center; color: orange;'>Rechercher par titre</h1>", unsafe_allow_html=True)

st.header("Vous pouvez effectuer votre recherche ci-dessous", divider = "orange")

movie_search = st.text_input("Nom du film:", value="")

# Filter the dataframe using masks
try:
    m1 = movie["title_x"].str.contains(movie_search, case = False)
    m2 = movie["originalTitle"].str.contains(movie_search, case = False)
    search = movie[m1 | m2].sort_values("popularity", ascending = False)
except:
    st.error("Nous n'avons malheureusement trouvé aucun film correspondant à votre recherche")

searching_list = []
# Show the results, if you have a text_search
if movie_search:
    if search.empty:
        st.error("Nous n'avons malheureusement trouvé aucun film correspondant à votre recherche")

    col1, col2, col3, col4, col5, col6, col7, col8, col9, col10, col11, col12, col13, col14, col15, col16 = st.columns(16)
    col = [col1, col2, col3, col4, col5, col6, col7, col8, col9, col10, col11, col12, col13, col14, col15, col16]
    
    for ind, numCol in enumerate(col):
        try:
            with numCol:
                cardNum = "card"+str(ind)
                cardNum = card(title = search['title_x'][search['title_x'] == search['title_x'].iloc[ind]].iloc[0],
                                text = search['genres_x'][search['title_x'] == search['title_x'].iloc[ind]].iloc[0],
                                image = 'https://image.tmdb.org/t/p/w500' + search['poster_path'][search['title_x'] == search['title_x'].iloc[ind]].iloc[0],
                                styles = {'card' :{'width': '80',
                                                    'height': '300px',
                                                    'border_radius': '10px',
                                                    'padding': '10px'},
                                        'text': {'font_family': 'Source Sans Pro'},
                                        'title': {'font_family': 'Source Sans Pro'}}
                                # on_click = lambda: st.switch_page('Pages/5_Vos_Recherches.py'),
                                )
                                # exec(f"card{ind} = card(title = {search['title_x'][search['title_x'] == search['title_x'].iloc[ind]].iloc[0]},"
                                # f"text = {search['genres_x'][search['title_x'] == search['title_x'].iloc[ind]].iloc[0]},"
                                # f"image = 'https://image.tmdb.org/t/p/w500' + {search['poster_path'][search['title_x'] == search['title_x'].iloc[ind]].iloc[0]},"
                                # f"styles = {'card' :{'width': '80',"
                                #                     f"'height': '300px',"
                                #                     f"'border_radius': '10px',"
                                #                     f"'padding': '10px'},"
                                #         f"'text': {'font_family': 'Source Sans Pro'},"
                                #         f"'title': {'font_family': 'Source Sans Pro'}},"
                                # f"on_click = lambda: st.switch_page('1_🍿_Accueil.py')")
        except:
            with numCol:
                st.write("")

# Test pour récupérer le session state -> ne fonctionne pas                

# st.session_state
# col1b, col2b = st.columns(2)
# with col1b:
#     cardTest = card(title = "Inception",
#                                 text = "",
#                                 image = "https://letsenhance.io/static/8f5e523ee6b2479e26ecc91b9c25261e/1015f/MainAfter.jpg",
#                                 styles = {"card" :{"width": "80",
#                                                     "height": "300px",
#                                                     "border_radius": "10px",
#                                                     "padding": "10px"},
#                                         "text": {"font_family": "Source Sans Pro"},
#                                         "title": {"font_family": "Source Sans Pro"}},
#                                 on_click = lambda: st.switch_page("Pages/5_Vos_Recherches.py"))

# with col2b:
#     cardTest2 = card(title = "Inception1",
#                                 text = "",
#                                 image = "https://letsenhance.io/static/8f5e523ee6b2479e26ecc91b9c25261e/1015f/MainAfter.jpg",
#                                 styles = {"card" :{"width": "80",
#                                                     "height": "300px",
#                                                     "border_radius": "10px",
#                                                     "padding": "10px"},
#                                         "text": {"font_family": "Source Sans Pro"},
#                                         "title": {"font_family": "Source Sans Pro"}},
#                                 on_click = lambda: st.switch_page("Pages/5_Vos_Recherches.py"))
