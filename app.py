import streamlit as st
import pickle
import requests
import pandas as pd


# Load movies and similarity data
movies = pickle.load(open('movie_with_posters.pkl', 'rb'))
similarity = pickle.load(open('similariy.pkl', 'rb'))


# Cache poster URLs to avoid repeated API calls
@st.cache_data



def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommendations = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommendations.append({
            'title': movies.iloc[i[0]].title,
            'poster': movies.iloc[i[0]].poster
        })
    return recommendations


# Streamlit UI
st.title('Movie Recommender System')
movie_list = movies['title'].values
option = st.selectbox("Select Your Favourite Movie", movie_list)

if st.button("Recommend"):
    recommendations = recommend(option)

    cols = st.columns(5)
    for idx, col in enumerate(cols):
        with col:
            st.text(recommendations[idx]['title'])
            st.image(recommendations[idx]['poster'])

