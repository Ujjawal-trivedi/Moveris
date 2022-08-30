import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
     response = requests.get("https://api.themoviedb.org/3/movie/{}?api_key=f1f8dafe875fbc2ce2af678be37f6c13&language=en-US".format(movie_id))
     data = response.json()
     return "https://image.tmdb.org/t/p/w500/" + data["poster_path"]


def recommend(movie):
     movie_index = movies[movies["title"] == movie].index[0]
     distances = similarity[movie_index]
     movies_list = sorted(list(enumerate(distances)), reverse=True , key = lambda x:x[1])[1:7]

     recomeneded_movies = []
     recomeneded_movies_poster = []
     for i in movies_list:
          movie_id = movies.iloc[i[0]].movie_id
          recomeneded_movies.append(movies.iloc[i[0]].title)

          #### now fetching poster from APi
          recomeneded_movies_poster.append(fetch_poster(movie_id))

     return recomeneded_movies,recomeneded_movies_poster

movies_dict = pickle.load(open("movies_dict.pkl","rb"))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open("similarity.pkl","rb"))

st.title("Movie Recommendation System")
st.markdown(
     f"""
    <style>
    .stApp {{
    background: url("https://img.freepik.com/premium-vector/movie-cinema-hall-theater-with-projection-wall_1017-11942.jpg?w=740");
    background-size: cover;
    background-repeat: no-repeat;


    }}
    </style>
    """,
     unsafe_allow_html=True
)
selected_movie_name = st.selectbox(
     'Which Movie would you like to see',
     movies["title"].values)

if st.button("Recommend"):
     recomeneded_movies , recomeneded_movies_poster = recommend(selected_movie_name)
     # for i in recommendations:
     #      st.write(i)

     col1, col2, col3 = st.columns(3)

     with col1:
          st.text(recomeneded_movies[0])
          st.image(recomeneded_movies_poster[0])

     with col2:
          st.text(recomeneded_movies[1])
          st.image(recomeneded_movies_poster[1])

     with col3:
          st.text(recomeneded_movies[2])
          st.image(recomeneded_movies_poster[2])

     col1, col2,col3 = st.columns(3)

     with col1:
          st.text(recomeneded_movies[3])
          st.image(recomeneded_movies_poster[3])

     with col2:
          st.text(recomeneded_movies[4])
          st.image(recomeneded_movies_poster[4])

     with col3:
          st.text(recomeneded_movies[5])
          st.image(recomeneded_movies_poster[5])