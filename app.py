import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=d988f0fb3e380c67acf3ef2cd3e5189c&language=en-US'.format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']


def recommend(movie):
    movie_index = movies[movies["title"] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:9]

    recomended_movie = []
    recomended_posters = []

    for i in movies_list:
        # fetching posters
        movie_id = movies.iloc[i[0]].id
        recomended_posters.append(fetch_poster(movie_id))
        # fetching movie name
        recomended_movie.append(movies.iloc[i[0]][1])
    return recomended_movie,recomended_posters



movies_list = pickle.load(open('movies_to_dict.pkl','rb'))
movies = pd.DataFrame(movies_list)


similarity = pickle.load(open('similarity.pkl','rb'))




st.title('Movie Recommendation System')

selected_movie_name = st.selectbox(
    'How would you like to be contacted?',
    movies['title'].values)




if st.button('Recommend'):
    names,posters = recommend(selected_movie_name)
    col1, col2, col3,  = st.columns(3)
    col4, col5, col6  = st.columns(3)

    with col1:
        st.image(posters[0])
        st.header(names[0])

    with col2:
        st.image(posters[1])
        st.header(names[1])

    with col3:
        st.image(posters[2])
        st.header(names[2])

    with col4:
        st.image(posters[3])
        st.header(names[3])

    with col5:
        st.image(posters[4])
        st.header(names[4])

    with col6:
        st.image(posters[5])
        st.header(names[5])

    # with co17:
    #     st.image(posters[6])
    #     st.text(names[6])

    # with col8:
    #     st.image(posters[7])
    #     st.text(names[7])

    # with col9:
    #     st.image(posters[8])
    #     st.text(names[8])

    # with co20:
    #     st.image(posters[9])
    #     st.text(names[9])
        

