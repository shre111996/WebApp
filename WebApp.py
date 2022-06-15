import streamlit as st
import pickle
import pandas as pd
import requests


# main function which performing the ml algorithm for recommendation
def recommand(selected_movie):
    index_of_the_movie = all_movies[all_movies.title == selected_movie]['index'].values[0]
    similarity_score = list(enumerate(similarity[index_of_the_movie]))
    sorted_movies = sorted(similarity_score, reverse=True, key=lambda x: x[1])
    j = 1
    suggested_movies = []
    poster_of_suggested_movie = []
    for movie in sorted_movies:
        # API for TMDB dataset
        # https://api.themoviedb.org/3/movie/movie_id?api_key=<<api_key>>&language=en-US
        index = movie[0]
        movie_id = all_movies[all_movies.index == index]['id'].values[0]
        title_from_index = all_movies[all_movies.index == index]['title'].values[0]
        if j <= 13:
            if title_from_index != selected_movie:
                suggested_movies.append(title_from_index)
                poster_of_suggested_movie.append(fetch_poster(movie_id))
            j += 1
    return suggested_movies, poster_of_suggested_movie


# For providing the poster of movies from TMDB website
def fetch_poster(index):
    response = requests.get(
        'https://api.themoviedb.org/3/movie/{}?api_key=d7f2371aba8c7bd6ffbf14c6aed89318&language=en-US'.format(index))
    poster_data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + poster_data['poster_path']


movie_dict = pickle.load(open('data/movie_dict.pkl', 'rb'))
all_movies = pd.DataFrame(movie_dict)
similarity = pickle.load(open('data/similarity.pkl', 'rb'))

# st.title('Minor Project')
st.header('Movie Recommendation System')

selected_movie_name = st.selectbox('Enter your favorite movie: ', all_movies['title'].values)
# Button function
m = st.markdown("""
<style>

div.stButton > button:first-child {
    background-color: #0000ff;
    color:#ffffff;
}
div.stButton > button:hover {
    background-color: rgb(0,0,0) ;
    color: #ffffff;
    border: none;
    }
</style>""", unsafe_allow_html=True)

# It will display the results
if st.button('Recommend'):
    name, poster = recommand(selected_movie_name)
    for i in range(1, 12, 4):
        a = i + 1
        b = i + 2
        c = i + 3
        coli, cola, colb, colc = st.columns(4)  # Number of movies shown in one row
        with coli:
            st.markdown(name[i - 1])
            st.image(poster[i - 1])
        with cola:
            st.markdown(name[a - 1])
            st.image(poster[a - 1])
        with colb:
            st.markdown(name[b - 1])
            st.image(poster[b - 1])
        with colc:
            st.markdown(name[c - 1])
            st.image(poster[c - 1])
