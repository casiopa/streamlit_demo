import streamlit as st
import numpy as np
import pandas as pd



st.sidebar.title('Sidebar title')

elementos = st.sidebar.selectbox(
    'Selecciona el tipo de elemento',
    ('Texto', 'Input Widgets', 'Gráficos'))



if elementos == 'Texto':
    st.title('Texto')
    
    st.subheader('text')
    st.text('Fixed width text')

    st.subheader('latex')
    st.latex(r''' e^{i\pi} + 1 = 0 ''')

    st.subheader('markdown')
    st.markdown('''
    ##### Lista markdown:
    - Elemento 1
    - Elemento 2
    - Elemento 3''')

    st.subheader('code')
    st.code('for i in range(8): foo()')




elif elementos =='Input Widgets':    
    st.title('Input Widgets')

    st.subheader('checkbox')
    if st.checkbox('Estoy de acuerdo', False):
        st.write('Estoy de acuerdo y se lleva a cabo la acción')


    st.subheader('selectbox')
    select = st.selectbox(
        'How would you like to be contacted?',
        ('Email', 'Home phone', 'Mobile phone'))

    st.write('You selected:', select)

    st.subheader('radio')
    radio = st.radio(
        'How would you like to be contacted?',
        ('Email', 'Home phone', 'Mobile phone'))

    st.write('You selected:', radio)


    st.subheader('number_input')
    number = st.number_input('Insert a number', 1, 10, step=1)
    st.write('The current number is ', number)


    st.subheader('multiselect')
    multi = st.multiselect(
        'What are your favorite colors',
        ['Green', 'Yellow', 'Red', 'Blue'],
        ['Yellow', 'Red'])

    st.write('You selected:', multi)


elif elementos == 'Gráficos': 
    st.title('Gráficos')

    st.subheader('line_chart')
    line_data = pd.DataFrame(np.random.randn(20, 3), columns=['a', 'b', 'c'])
    st.line_chart(line_data)

    st.subheader('bar_chart')
    bar_data = pd.DataFrame(np.random.randn(50, 3), columns=["a", "b", "c"])
    st.bar_chart(bar_data)

    st.subheader('map')
    map_df = pd.DataFrame(np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4], columns=['lat', 'lon'])
    st.map(map_df)
