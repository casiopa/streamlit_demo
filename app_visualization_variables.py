intro = '''
# Público, crítica y taquilla en IMDb
### Análisis exploratorio de datos | Películas 2014 a 2019
El objetivo de este estudio es buscar relaciones entre las valoraciones de usuario y de críticos del cine, y las características económicas de las películas como el presupuesto y la recaudación conseguida.
Con la intención de analizar datos representativos de todo tipo de películas se ha acudido al portal IMDb, el más completo a nivel internacional, y se han extraído los datos por dos vías: la descarga de tablas relacionales gratuitas de IMDb y mediante *web scrapping* de las películas del portal IMDb. El alcance de este estudio está limitado por la información accesible de manera gratuita en el portal IMDb, y a nivel temporal, se centra en los años comprendidos entre 2014 y 2019.
El objetivo inicial era estudiar los 10 años anteriores a 2020 (de 2010 a 2019) pero por falta de recursos solo ha sido posible recoger datos para 6 años (2014 a 2019).

'''


intro_herramientas_fuentes = '''
---
## Herramientas utilizadas

| Web scrapping 		| Data mining		| Visualización  	|
|---					|---				|---				|
| - Visual Studio Code	| - Jupyter Lab		| - Streamlit		|
| - Python				| - Python			| - Python			|
| - Pandas				| - Regex			| - Regex			|
| - Selenium			| - Pandas			| - Pandas			|
| - Joblib / Parallel	| - Numpy			| - Numpy			|
| - Logging				|   				| - Matplotlib		|
| - Pickle				|   				| - Plotly			|
|   					|   				| - Google Slides	|


---
## Fuentes

IMDd Datasets
https://datasets.imdbws.com/

IMDb. Documentación para los datasets:
https://www.imdb.com/interfaces/

OECD. Tasas de cambio principales monedas por año:
https://data.oecd.org/conversion/exchange-rates.htm

Exchange Rates.Tasas de cambio otras monedas por año:
https://www.exchangerates.org.uk/

Google Developers. Listado de coordenadas de países:
https://developers.google.com/public-data/docs/canonical/countries_csv


'''