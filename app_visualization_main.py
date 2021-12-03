import streamlit as st
from app_visualization_functions import *


st.set_page_config(page_title='Streamlit Demo',
                   page_icon='https://www.google.com/s2/favicons?domain=www.imdb.com',
                   layout="wide")

# Pone el radio-button en horizontal. Afecta a todos los radio button de una página.
# Por eso está puesto en este que es general a todo
st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)


st.sidebar.image('images/800px-IMDB_Logo_2016.svg.png', width=200)
st.sidebar.header('Público, crítica y taquilla en IMDb')
st.sidebar.markdown('Análisis exploratorio de datos | Películas 2014 a 2019')


menu = st.sidebar.radio(
    "",
    ("Intro", "Data", "Relaciones entre variables", "Matrices de correlación"),
)


st.sidebar.markdown('---')
st.sidebar.write('Ana Blanco | Julio 2021 anablancodelgado@gmail.com https://casiopa.github.io/')


if menu == 'Intro':
    #set_home()
    pass
elif menu == 'Data':
    #set_data()
    pass
elif menu == 'Relaciones entre variables':
    #set_relations()
    pass
elif menu == 'Matrices de correlación':
    #set_arrays()
    pass
