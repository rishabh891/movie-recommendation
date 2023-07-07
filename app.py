import streamlit as st
import pickle
import pandas as pd
import requests


def fetch_poster(movie_id):
    response = requests.get(
        'https://api.themoviedb.org/3/movie/{}?api_key=1ba535e0ef49d30a42c7a01234923f16'.format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/original" + data['poster_path']


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:7]
    recommended_movies = []
    recommended_movie_poster = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].id

        recommended_movies.append((movies.iloc[i[0]].title))
        recommended_movie_poster.append(fetch_poster(movie_id))
    return recommended_movies, recommended_movie_poster


similarity = pickle.load(open("similarity.pkl", 'rb'))
movies_dict = pickle.load(open("movie_dict.pkl", 'rb'))
movies = pd.DataFrame(movies_dict)
st.title("Movies Recommender System")
selected_movie_name = st.selectbox("Enter the name of movie", (movies['title'].values))
if st.button("Recommend"):
    name, poster = recommend(selected_movie_name)
    col1, col2 = st.columns(2)
    with col1:
        st.subheader(name[0])
        st.image(poster[0])
    with col2:
        st.subheader(name[1])
        st.image(poster[1])
    col3, col4 = st.columns(2)
    with col3:
        st.subheader(name[2])
        st.image(poster[2])

    with col4:
        st.subheader(name[3])
        st.image(poster[3])
    col5, col6 = st.columns(2)
    with col5:
        st.subheader(name[4])
        st.image(poster[4])
    with col6:
        st.subheader(name[5])
        st.image(poster[5])
