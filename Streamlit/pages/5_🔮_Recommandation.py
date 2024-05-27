import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_card import card
import df_call

# Modifying the page title and icon
st.set_page_config(page_title = "Le Senechal - Reco", page_icon = "🔮", layout = "wide")

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

st.markdown("<h1 style='text-align: center; color: orange;'>Rechercher par titre</h1>", unsafe_allow_html=True)
movie = df_call.df_final()
name = df_call.name_df()

st.header("Vous pouvez effectuer votre recherche ci-dessous", divider = "orange")

selection = st.selectbox("Choisissez votre film", movie["title_x"], index = None)

# --------------------------- TO DO -------------------------
# Checker les films homonymes!
# movie[movie["title_x"] == selection]
# -----------------------------------------------------------

if selection != None:
    director = movie["director1"][movie["title_x"] == selection].iloc[0]
    actor1 = movie["actor1"][movie["title_x"] == selection].iloc[0]
    actor2 = movie["actor2"][movie["title_x"] == selection].iloc[0]
    actor3 = movie["actor3"][movie["title_x"] == selection].iloc[0]

    col1, col2 = st.columns([0.4, 0.6])
    
    try:

        with col1:
            card_one = card(title = movie["title_x"][movie["title_x"] == selection].iloc[0],
                            text = movie["genres_x"][movie["title_x"] == selection].iloc[0],
                            image = "https://image.tmdb.org/t/p/w500" + movie["poster_path"][movie["title_x"] == selection].iloc[0],
                            styles = {"card" :{"width": "300",
                                                "height": "300px",
                                                "border_radius": "10px"},
                                    "text": {"font_family": "Source Sans Pro, sans serif"},
                                    "title": {"font_family": "Source Sans Pro"}})
        
    except:
        if selection != None:
            with col1:
                st.markdown("<h1 style='text-align: center; color: orange;'> <br> </h1>", unsafe_allow_html=True)
                st.subheader(movie["title_x"][movie["title_x"] == selection].iloc[0])
    try:        
        with col2:
            st.markdown("<h1 style='text-align: center; color: orange;'> <br> </h1>", unsafe_allow_html=True)
            st.write("Runtime: " + str(movie["runtimeMinutes"][movie["title_x"] == selection].iloc[0]) + " min")
            st.write("Rating: " + str(movie["averageRating"][movie["title_x"] == selection].iloc[0]) + "/10")
            st.write("Released in : " + str(movie["release_date"][movie["title_x"] == selection].iloc[0]))
            st.subheader("Director:")
            st.write(name["primaryName"][name["nconst"] == director].iloc[0])
            st.subheader("Starring:")
            st.write(name["primaryName"][name["nconst"] == actor1].iloc[0] + ", " + name["primaryName"][name["nconst"] == actor2].iloc[0] + ", " + name["primaryName"][name["nconst"] == actor3].iloc[0])
    except:
        st.write("")
    st.subheader("Synopsis:")
    st.write(movie["overview"][movie["title_x"] == selection].iloc[0])



if selection != None:
    st.header("Films similaires:")
        
    reco = df_call.ML_Reco(movie["tconst"][movie["title_x"] == selection].iloc[0])


    col1, col2, col3, col4, col5, col6, col7, col8, col9, col10, col11, col12, col13, col14, col15, col16 = st.columns(16)
    col = [col1, col2, col3, col4, col5, col6, col7, col8, col9, col10, col11, col12, col13, col14, col15, col16]

    for ind, movie_name in enumerate(reco):
        try:
            with col[ind + 1]:
                cardNum = card(title = movie['title_x'][movie['title_x'] == movie_name].iloc[0],
                                text = movie['genres_x'][movie['title_x'] == movie_name].iloc[0],
                                image = 'https://image.tmdb.org/t/p/w500' + movie['poster_path'][movie['title_x'] == movie_name].iloc[0],
                                styles = {'card' :{'width': '80',
                                                    'height': '300px',
                                                    'border_radius': '10px',
                                                    'padding': '10px'},
                                        'text': {'font_family': 'Source Sans Pro'},
                                        'title': {'font_family': 'Source Sans Pro'}})

        except:
            with col[ind + 1]:
                st.write("")



# --------- Old code ------------------------
# movie_search = st.selectbox("Choisissez votre film", movie["title_x"])

# # Filter the dataframe using masks
# try:
#     m1 = movie["title_x"].str.contains(movie_search, case = False)
#     m2 = movie["originalTitle"].str.contains(movie_search, case = False)
#     search = movie[m1 | m2].sort_values("popularity", ascending = False)
# except:
#     st.error("Nous n'avons malheureusement trouvé aucun film correspondant à votre recherche")

# # Show the results, if you have a text_search
# if movie_search:
#     if search.empty:
#         st.error("Nous n'avons malheureusement trouvé aucun film correspondant à votre recherche")

#     selection = st.selectbox("Choisissez votre film", search["title_x"])
    
#     director = search["director1"][search["title_x"] == selection].iloc[0]
#     actor1 = search["actor1"][search["title_x"] == selection].iloc[0]
#     actor2 = search["actor2"][search["title_x"] == selection].iloc[0]
#     actor3 = search["actor3"][search["title_x"] == selection].iloc[0]
    
#     try:
#         col1, col2 = st.columns([0.4, 0.6])
#         with col1:
#             card_one = card(title = search["title_x"][search["title_x"] == selection].iloc[0],
#                             text = search["genres_x"][search["title_x"] == selection].iloc[0],
#                             image = "https://image.tmdb.org/t/p/w500" + search["poster_path"][search["title_x"] == selection].iloc[0],
#                             styles = {"card" :{"width": "300",
#                                                 "height": "300px",
#                                                 "border_radius": "10px"},
#                                     "text": {"font_family": "Source Sans Pro, sans serif"},
#                                     "title": {"font_family": "Source Sans Pro"}})
#         with col2:
#             st.markdown("<h1 style='text-align: center; color: orange;'> <br> </h1>", unsafe_allow_html=True)
#             st.subheader("Rating:")
#             st.write(search["averageRating"][search["title_x"] == selection].iloc[0])
#             st.write("Released in :" + str(search["release_date"][search["title_x"] == selection].iloc[0]))
#             st.subheader("Director:")
#             st.write(name["primaryName"][name["nconst"] == director].iloc[0])
#             st.subheader("Starring:")
#             st.write(name["primaryName"][name["nconst"] == actor1].iloc[0] + ", " + name["primaryName"][name["nconst"] == actor2].iloc[0] + ", " + name["primaryName"][name["nconst"] == actor3].iloc[0])
#             # st.subheader("Runtime:")
#             # st.write(search["runtimeMinutes"][search["title_x"] == selection].iloc[0])
        
#         st.subheader("Synopsis:")
#         st.write(search["overview"][search["title_x"] == selection].iloc[0])

        
#     except:
#         st.write("")
        
#     st.header("Films similaires:")
    
#     reco = df_call.ML_Reco(search["tconst"][search["title_x"] == selection].iloc[0])
    
    
#     col1, col2, col3, col4, col5, col6, col7, col8, col9, col10, col11, col12, col13, col14, col15, col16 = st.columns(16)
#     col = [col1, col2, col3, col4, col5, col6, col7, col8, col9, col10, col11, col12, col13, col14, col15, col16]
    
#     for ind, movie_name in enumerate(reco):
#         try:
#             with col[ind + 1]:
#                 cardNum = card(title = movie['title_x'][movie['title_x'] == movie_name].iloc[0],
#                                 text = movie['genres_x'][movie['title_x'] == movie_name].iloc[0],
#                                 image = 'https://image.tmdb.org/t/p/w500' + movie['poster_path'][movie['title_x'] == movie_name].iloc[0],
#                                 styles = {'card' :{'width': '80',
#                                                     'height': '300px',
#                                                     'border_radius': '10px',
#                                                     'padding': '10px'},
#                                         'text': {'font_family': 'Source Sans Pro'},
#                                         'title': {'font_family': 'Source Sans Pro'}})

#         except:
#             with col[ind + 1]:
#                 st.write("")
