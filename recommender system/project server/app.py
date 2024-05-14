import streamlit as st
import pickle
import pandas as pd
import requests
# def fetch_poster(movie_id):
#     url = 'https://api.themoviedb.org/3/movie/{}?api_key=ffaf8b927365934ceb51c657fac47b1c&language=en-US%22'.format(movie_id)
#     data = requests.get(url)
#     data = data.json()
#     poster_path = data['poster_path']
#     full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
#     return full_path
st.title("Movie Recommender System")
movie_dict = pickle.load(open('movie_dict.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))
movies = pd.DataFrame(movie_dict)
def recommend(movie):
    movie_index = movies[movies.title == movie].index[0]
    distance = similarity[movie_index]
    movies_list = sorted(list(enumerate(distance)),reverse=True,key=lambda x :x[1])[1:6]
    rec_mov = []
    rec_mov_pos = []
    for i in movies_list:
        # movie_id = movies['movie_id'][i[0]]
        rec_mov.append(movies.title[i[0]])
        #fetch movie poster
        # rec_mov_pos.append(fetch_poster(movie_id))
    return rec_mov
option = st.selectbox(
    "How would you like to be contacted?",
    movies.title.values)

if st.button('Recommand'):
    # recomendations,poster  = recommend(option)
    for i in recommend(option):
        st.text(i)
   
    # col1, col2, col3, col4, col5 = st.beta_columns(5)
    # with col1:
    #     st.text(recomendations[0])
    #     st.image(poster[0])
    # with col2:
    #     st.text(recomendations[1])
    #     st.image(poster[1])

    # with col3:
    #     st.text(recomendations[2])
    #     st.image(poster[2])
    # with col4:
    #     st.text(recomendations[3])
    #     st.image(poster[3])
    # with col5:
    #     st.text(recomendations[4])
    #     st.image(poster[4])
