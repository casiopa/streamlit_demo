import streamlit as st
import pandas as pd
from app_visualization_variables import *
from app_visualization_graphics import *


@st.cache(persist=True)
def load_csv():
    data = pd.read_csv('data/movies.csv', sep=';')
    return data


def set_home():
    md_parasite = 'https://m.media-amazon.com/images/M/MV5BYWZjMjk3ZTItODQ2ZC00NTY5LWE0ZDYtZTI3MjcwN2Q5NTVkXkEyXkFqcGdeQXVyODk4OTc3MTY@._V1_FMjpg_UY720_.jpg'
    md_boyhood = 'https://m.media-amazon.com/images/M/MV5BMTYzNDc2MDc0N15BMl5BanBnXkFtZTgwOTcwMDQ5MTE@._V1_FMjpg_UX1000_.jpg'
    md_endgame = 'https://m.media-amazon.com/images/M/MV5BMTc5MDE2ODcwNV5BMl5BanBnXkFtZTgwMzI2NzQ2NzM@._V1_FMjpg_UY720_.jpg'
    md_interstellar = 'https://m.media-amazon.com/images/M/MV5BZjdkOTU3MDktN2IxOS00OGEyLWFmMjktY2FiMmZkNWIyODZiXkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_FMjpg_UY720_.jpg'
    md_showman = 'https://m.media-amazon.com/images/M/MV5BYjQ0ZWJkYjMtYjJmYS00MjJiLTg3NTYtMmIzN2E2Y2YwZmUyXkEyXkFqcGdeQXVyNjk5NDA3OTk@._V1_FMjpg_UY720_.jpg'
    md_split = 'https://m.media-amazon.com/images/M/MV5BZTJiNGM2NjItNDRiYy00ZjY0LTgwNTItZDBmZGRlODQ4YThkL2ltYWdlXkEyXkFqcGdeQXVyMjY5ODI4NDk@._V1_FMjpg_UY720_.jpg'
    md_sw_despertar = 'https://m.media-amazon.com/images/M/MV5BOTAzODEzNDAzMl5BMl5BanBnXkFtZTgwMDU1MTgzNzE@._V1_FMjpg_UY720_.jpg'
    md_lalaland = 'https://m.media-amazon.com/images/M/MV5BMzUzNDM2NzM2MV5BMl5BanBnXkFtZTgwNTM3NTg4OTE@._V1_FMjpg_UY720_.jpg'

    col1, col2, col3, col4, col5, col6, col7, col8 = st.columns(8)

    with col1:
        st.image(md_parasite, use_column_width='always')
    with col2:
        st.image(md_endgame, use_column_width='always')
    with col3:
        st.image(md_showman, use_column_width='always')
    with col4:
        st.image(md_interstellar, use_column_width='always')
    with col5:
        st.image(md_boyhood, use_column_width='always')
    with col6:
        st.image(md_split, use_column_width='always')
    with col7:
        st.image(md_sw_despertar, use_column_width='always')
    with col8:
        st.image(md_lalaland, use_column_width='always')

    st.write(intro)
    st.write(intro_herramientas_fuentes)


def set_data():
    movies = load_csv()

    st.title('Data')
    col1, col2 = st.columns(2)

    with col1:
        st.markdown('### Nº de películas en IMDb')
        st.markdown('117.482 páginas de películas (2014-2020) escrapeadas del portal IMDb')
        st.markdown(' ')
        st.pyplot(bars_nmovies_imdb())

    with col2:
        st.markdown('### Nº de películas de IMDb filtradas')
        st.markdown('Datos resultantes tras filtrar las películas con rating, metascore, presupuesto o recaudación. 1.553 películas')
        st.pyplot(bars_nmovies(movies))

    st.markdown('### DataFrame `movies`')
    st.markdown('DataFrame final preparado para el estudio tras filtrar las películas con rating, metascore, presupuesto o recaudación. 1.553 películas.')
    st.markdown('1.553 entries  |  24 columns')
    st.dataframe(movies)


def set_relations():
    movies = load_csv() 
    st.title('Relaciones entre variables')

    menu_relations= st.radio(
        "",
        ("Rating/Metascore", "R/M/Presupuesto", "R/M/Presupuesto/Beneficio", "R/M/Presupuesto/ROI"),
    )

    if menu_relations == "Rating/Metascore":

        st.markdown('### Relación entre Rating y Metascore')
        st.write(scatter_rating_metascore(movies))
        
    elif menu_relations == "R/M/Presupuesto":

        st.markdown('### Relación entre Rating, Metascore y Presupuesto (tamaño)')
        st.write(scatter_rating_metascore(movies, size='budget'))
       
    elif menu_relations == "R/M/Presupuesto/Beneficio":

        st.markdown('### Relación entre Rating, Metascore, Presupuesto (tamaño) y Beneficio (color)')
        st.write(scatter_rating_metascore(movies, size='budget', color='profit', title_color = 'Beneficio'))
       
    elif menu_relations == "R/M/Presupuesto/ROI":

        st.markdown('### Relación entre Rating, Metascore, Presupuesto (tamaño) y ROI (color)')
        st.write(scatter_rating_metascore(movies, size='budget', color='roi', title_color = 'ROI'))



def set_arrays():
    movies = load_csv() 

    st.title('Matrices de correlación')

    corr_6x6 = movies[movies.roi<30][['ratingImdb', 'metascore', 'budget', 'grossWorld', 'profit', 'roi']].corr()
    corr_2x4 = corr_6x6.loc['ratingImdb': 'metascore', 'budget':'roi']

    menu_arrays= st.radio(
        "",
        ("6x6", "2x4", "Géneros", "Países"),
    )

    if menu_arrays == "6x6":
        st.write(heatmap_6x6(corr_6x6))
    elif menu_arrays == "2x4":
        st.write(heatmap_2x4(corr_2x4))

    elif menu_arrays == 'Géneros':

        menu_genre = st.radio(
            "",
            ('Action', 'Drama', 'Comedy', 'Bio-Documentary', 'Adventure', 'Thriller', 'Horror', 'Animation')
        )
        movies_genre = movies.copy()
        movies_genre = primaryGenre(movies_genre)
        corr_genre = movies_genre[(movies_genre.roi<30) & (movies_genre.primaryGenre==menu_genre)][['ratingImdb', 'metascore', 'budget', 'grossWorld', 'profit', 'roi']].corr().loc['ratingImdb': 'metascore', 'budget':'roi']
        st.write(heatmap_2x4(corr_genre))


    elif menu_arrays == 'Países':
        movies_countries = movies.copy()
        
        menu_country = st.radio(
            "",
            ('United States', 'United Kingdom', 'France', 'Canada', 'China', 'Spain')
        )

        movies_countries['primaryCountry'] = movies_countries['countries'].apply(first_elem_csv)
        corr_country = movies_countries[(movies_countries.roi<30) & (movies_countries.primaryCountry==menu_country)][['ratingImdb', 'metascore', 'budget', 'grossWorld', 'profit', 'roi']].corr().loc['ratingImdb': 'metascore', 'budget':'roi']
        st.write(heatmap_2x4(corr_country))
