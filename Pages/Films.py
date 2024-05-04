import streamlit as st
import pandas as pd
import plotly.express as px


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
            </style>
            """, unsafe_allow_html=True)

link = r"C:\Users\User\Wild_Code\Projects\Project_2\DB\tmdb_full.csv"
tmdb = pd.read_csv(link, low_memory = False)

# tmdb[tmdb["original_title"].str.contains("star wars", case = False)]
st.title("Voici la page de recherche et recommandation de films")
st.header("Vous pouvez choisir par type de films")

movie_search = st.text_input("Recherche par titre ou par genre", value="")

# Filter the dataframe using masks
m1 = tmdb["title"].str.contains(movie_search, case = False)
m2 = tmdb["original_title"].str.contains(movie_search, case = False)
m3 = tmdb["genres"].str.contains(movie_search, case = False)
tmdb_search = tmdb[m1 | m2 | m3]

searching_list = []
# Show the results, if you have a text_search
if movie_search:
    st.write(tmdb_search.sort_values("vote_average", ascending = False))
    searching_list.append(movie_search)
    

# st.image("https://image.tmdb.org/t/p/w500/6FfCtAuVAW8XJjZ7eWeLibRLWTw.jpg")
# # st.image("https://www.themoviedb.org/t/p/w600_and_h900_bestv2/6FfCtAuVAW8XJjZ7eWeLibRLWTw.jpg")

# st.write("Synopsis:")
# tmdb["overview"][tmdb["original_title"].str.contains("star wars", case = False)].iloc[0]

# st.image("https://www.themoviedb.org/t/p/w600_and_h900_bestv2/6wkfovpn7Eq8dYNKaG5PY3q2oq6.jpg")

searching_list