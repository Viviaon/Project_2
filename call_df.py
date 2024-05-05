import pandas as pd
import numpy as np

def movie_df():
            # Read the right files to create our DB
            
            link_bas = "https://datasets.imdbws.com/title.basics.tsv.gz"
            title_bas = pd.read_csv(link_bas, sep = "\t", low_memory = False, na_values = r"\N")
            
            link_akas = "https://datasets.imdbws.com/title.akas.tsv.gz"
            title_akas = pd.read_csv(link_akas, sep = "\t", low_memory = False, na_values = r"\N")
            
            link_rate = "https://datasets.imdbws.com/title.ratings.tsv.gz"
            title_rate = pd.read_csv(link_rate, sep = "\t", na_values = r"\N")
            
            TMdb = pd.read_csv("https://drive.google.com/file/d/1VB5_gl1fnyBDzcIOXZ5vUSbCY68VZN1v/view", low_memory = False)

            # Creation of the DB with only movies without genre Adult
            df_movie = title_bas[(~title_bas["genres"].str.contains("Adult", na = False)) & (title_bas["titleType"].str.contains("movie", na = False))]
            
            # Creation of the list of traduced title
            fr_akas = title_akas[["titleId","title", "types", "region"]][title_akas["region"].str.contains("FR", na = False)]
            
            # Add the title type on akas to filter just the movies
            fr_akas = fr_akas.merge(title_bas["titleType"], how = "left", left_on = fr_akas["titleId"], right_on = title_bas["tconst"])
            fr_akas = fr_akas[fr_akas["titleType"] == "movie"]
            
            # Remove duplicated akas in FR
            dupli_akas = fr_akas[fr_akas.duplicated(subset = "titleId", keep = False)]
            dupli_akas["types"] = dupli_akas["types"].apply(lambda x: "aaimdbDisplay" if x == "imdbDisplay" else x)
            dupli_akas.sort_values(by = "types", inplace = True)
            # Removing the duplicated lines (same movie with different fr akas)
            dupli_akas.drop_duplicates(subset = ["titleId"], inplace = True)
            # Removing all duplicated lines (same movie with different fr akas)
            fr_akas.drop_duplicates(subset = ["titleId"], keep = False, inplace = True)
            # Add the unique title from the duplicated list 
            fr_akas = pd.concat([fr_akas, dupli_akas])
            
            # Merging (INNER) movies and akas to get only the translated movies
            movies_frt = df_movie.merge(fr_akas["title"], how = "inner", left_on = df_movie["tconst"], right_on = fr_akas["titleId"])
            movies_frt.drop(columns = "key_0", inplace = True)
            # Merging (LEFT) fr_movies with ratings
            movies_frt = movies_frt.merge(title_rate[["averageRating", "numVotes"]], how = "left", left_on = movies_frt["tconst"], right_on = title_rate["tconst"])
            movies_frt.drop(columns = "key_0", inplace = True)
            
            # Final selection of movies before dropping columns
            movie_final = movies_frt.merge(TMdb, how = "left", left_on = movies_frt["tconst"], right_on = TMdb["imdb_id"])
            
            to_add = movie_final[(movie_final["genres_x"].isna()) & (movie_final["genres_y"].notna()) & (movie_final["genres_y"] != "[]")]
            movie_final.drop(movie_final[movie_final["genres_x"].isna()].index, inplace = True)
            movie_final = pd.concat([movie_final, to_add])
            
            return movie_final
