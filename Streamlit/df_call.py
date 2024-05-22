import pandas as pd
import numpy as np


def df_final():
    link = r"C:\Users\User\Wild_Code\Projects\Project_2\App\movie_final_ML.csv"
    df_movie = pd.read_csv(link, low_memory = False, index_col = "Unnamed: 0")
    
    return df_movie


def name_df():
    link = r"C:\Users\User\Wild_Code\Projects\Project_2\App\name_list.csv"
    df_name = pd.read_csv(link, low_memory = False)
    
    return df_name