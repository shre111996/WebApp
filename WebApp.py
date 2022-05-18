import streamlit as st
# For running your web app command :-
# streamlit run file_name.py
import pickle
import pandas as pd
import requests

def recommand(selected_movie):
    index_of_the_movie = all_movies[all_movies.title == selected_movie]['index'].values[0]
    similarity_score = list(enumerate(similarity[index_of_the_movie]))
    sorted_movies = sorted(similarity_score, reverse=True, key=lambda x: x[1])
    i = 1
    suggested_movies = []
    poster_of_suggested_movie = []
    for movie in sorted_movies:
        # API for TMDB dataset
        # https://api.themoviedb.org/3/movie/movie_id?api_key=<<api_key>>&language=en-US
        index = movie[0]
        movie_id = all_movies[all_movies.index == index]['id'].values[0]
        title_from_index = all_movies[all_movies.index == index]['title'].values[0]
        if i <= 13:
            if title_from_index != selected_movie:
                suggested_movies.append(title_from_index)
                poster_of_suggested_movie.append(fetch_poster(movie_id))
            i += 1
    return suggested_movies, poster_of_suggested_movie


def fetch_poster(index):
    response = requests.get(
        'https://api.themoviedb.org/3/movie/{}?api_key=d7f2371aba8c7bd6ffbf14c6aed89318&language=en-US'.format(index))
    poster_data = response.json()
    # st.text(poster_data)
    # st.text('https://api.themoviedb.org/3/movie/{}?api_key=d7f2371aba8c7bd6ffbf14c6aed89318&language=en-US'.format(index))
    return "https://image.tmdb.org/t/p/w500/" + poster_data['poster_path']

movie_dict = pickle.load(open('data/movie_dict.pkl', 'rb'))
all_movies = pd.DataFrame(movie_dict)
similarity = pickle.load(open('data/similarity.pkl', 'rb'))

st.title('Bezzie Minor Project')
st.subheader('Movie Recommendation System')

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
if st.button('Recommend'):
    name, poster = recommand(selected_movie_name)
    col1,col2,col3,col4 = st.columns(4)
    with col1:
        st.markdown(name[0])
        st.image(poster[0])
    with col2:
        st.markdown(name[1])
        st.image(poster[1])
    with col3:
        st.markdown(name[2])
        st.image(poster[2])
    with col4:
        st.markdown(name[3])
        st.image(poster[3])

    col5,col6, col7, col8 = st.columns(4)
    with col5:
        st.markdown(name[4])
        st.image(poster[4])
    with col6:
        st.markdown(name[5])
        st.image(poster[5])
    with col7:
        st.markdown(name[6])
        st.image(poster[6])
    with col8:
        st.markdown(name[7])
        st.image(poster[7])
    col9, col10,col11,col12 = st.columns(4)
    with col9:
        st.markdown(name[8])
        st.image(poster[8])
    with col10:
        st.markdown(name[9])
        st.image(poster[9])
    with col11:
        st.markdown(name[10])
        st.image(poster[10])
    with col12:
        st.markdown(name[11])
        st.image(poster[11])