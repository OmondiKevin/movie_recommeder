"""This module uses pandas to further clean the data by filling in the missing values in the Rating, creates a user
movie matrix and finally passes the parameters to the recommendation function
The notebook for this module was saved as Scratch file therefore not available for Git.
"""

import pandas as pd
import numpy as np
from main import CLEAN_DATA
from tasks import read_json_from_file
from sklearn.metrics.pairwise import cosine_similarity

df = pd.DataFrame(read_json_from_file(f'{CLEAN_DATA}cleaned_data.json'))
df["Rating"] = df["Rating"].fillna(df['Rating'].mean(), inplace=True)

user_ids = df['User'].astype('category').cat.codes
movie_ids = df['Movie'].astype('category').cat.codes

user_movie_matrix = pd.pivot_table(df, values='Rating', index=user_ids, columns=movie_ids, fill_value=0)
user_similarity = cosine_similarity(user_movie_matrix)


def recommend_movies_with_names(user, top_n=5):
    user_id = user_ids[df['User'] == user].values[0]
    user_ratings = user_movie_matrix.loc[user_id]

    similar_users = user_similarity[user_id].argsort()[::-1][1:]
    weighted_sum = np.dot(user_similarity[user_id, similar_users], user_movie_matrix.iloc[similar_users].values)

    predicted_ratings = weighted_sum / np.sum(np.abs(user_similarity[user_id, similar_users]))
    unrated_movies = user_ratings[user_ratings == 0].index
    recommendations = pd.Series(predicted_ratings, index=user_movie_matrix.columns)[unrated_movies].sort_values(
        ascending=False)

    movie_names = df['Movie'].unique()[recommendations.index]

    recommended_movies = pd.DataFrame({
        'Movie': movie_names,
        'Predicted Rating': recommendations.values
    }).head(top_n)

    return recommended_movies

