import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.figure_factory as ff


def bars_nmovies(movies):
    plt.style.use('dark_background')

    #prepare data
    nmovies = movies.groupby('year')['year'].count()

    fig, ax = plt.subplots(figsize=(8,3.5))

    ax.bar(nmovies.index.astype(int), nmovies.values, color = '#f5c518', edgecolor = "none")

    ax.set_yticks([])
    ax.spines['bottom'].set_linewidth(2)
    ax.spines['left'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.xaxis.grid(False)

    plt.xticks(nmovies.index.astype(int), fontsize=12)

    # Pintar valores sobre las barras
    for anno, peli in tuple(zip(nmovies.index.astype(int), nmovies.values)):
        ax.text(anno, peli+10, '{0:,}'.format(peli).replace(',', '.'), va='bottom', ha = 'center', fontsize = 18, fontweight = 'regular')

    return fig


def bars_nmovies_imdb():
    # Número de pelis por año en IMDb
    n_pelis = [12218, 13148, 14105, 14791, 15862, 16412, 17609, 17967, 17819, 17181, 14632, 11842]

    annos = np.arange(2010,2022)

    plt.style.use('dark_background')

    fig, ax = plt.subplots(figsize=(13,6.3))

    ax.bar(annos, n_pelis, edgecolor = "none",
        color = ['#777', '#777', '#777', '#777', '#f5c518', '#f5c518', '#f5c518', '#f5c518', '#f5c518', '#f5c518', '#777', '#444'])

    ax.set_yticks([])
    ax.spines['bottom'].set_linewidth(2)
    ax.spines['left'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.xaxis.grid(False)

    annos_xticks = annos.astype(str)
    annos_xticks[11] = 'jun\n2021'
    plt.xticks(annos, labels=annos_xticks, fontsize=12)

    # Pintar valores sobre las barras
    for anno, peli in tuple(zip(annos, n_pelis)):
        ax.text(anno, peli+200, '{0:,}'.format(peli).replace(',', '.'), va='bottom', ha = 'center', fontsize = 14, fontweight = 'regular');
    
    return fig




def scatter_rating_metascore(movies, size=None, color=None, title_color=''):
    gris = '#999'

    fig = px.scatter(movies[movies.roi<30],
                     x="ratingImdb", y="metascore", color=color, size=size,
                     width=780, height=780, opacity=0.5,
                     color_continuous_scale=["#F5C518", "#F91949"],
                     template="plotly_dark",
                     hover_name="spanishTitle", hover_data=["ratingImdb", "metascore"]
                )
    
    if color == None:
        fig.update_traces(marker=dict(color="#F5C518"))

    fig.update_layout(coloraxis_colorbar = dict(title=title_color,
                                              ),
                      legend = dict(title = 'legend', font = {'size':14}),
                      title = dict(font = {'size':20, 'color': "#F5C518"}),
                     )

    fig.update_xaxes(
        title_text = "Rating de IMDb (1-10)",
        title_font = {"size": 15},
        title_standoff = 20,
        showgrid = False,
        showline = False,
        showticklabels = False,
        zeroline = False
    )

    fig.update_yaxes(
        title_text = "Metascore (1-100)",
        title_font = {"size": 15},
        title_standoff = 20,
        showgrid = False,
        showline = False,
        showticklabels = False,
        zeroline = False
    )

    fig.add_shape( # línea horizontal
        type="line", line_color=gris, line_width=1, opacity=1,
        x0=0, x1=10, xref="x", y0=50, y1=50, yref="y"
    )

    fig.add_annotation( # texto línea horizontal  
        text="Suspenso Metascore", x=1.3, y=48, showarrow=False, font = {'color': gris, 'size':14}
    )

    fig.add_shape( # línea vertical
        type="line", line_color=gris, line_width=1, opacity=1,
        x0=5, x1=5, xref="x", y0=0, y1=100, yref="y"
    )

    fig.add_annotation( # texto línea vertical  
        text="Suspenso Rating IMDb", x=3.5, y=-2, showarrow=False, font = {'color': gris, 'size':14}
    )

    return fig





### Devuelve el primer elemento de una lista
def first_elem_csv(csv):
    if str(csv) == 'nan':
        return np.nan
    else:
        return csv.split(',')[0]


### Agrupación de los géneros en 6 categorías
def grouppingGenres(genre):
    if (genre == 'Biography') | (genre == 'Documentary'):
        return 'Bio-Documentary'
    elif genre == 'Crime':
        return 'Thriller'
    elif genre == 'Fantasy':
        return 'Adventure'
    elif genre == 'Family':
        return 'Adventure'
    else:
        return genre


### Prepare variable genre with 1 genre of 6 posibble categories
def primaryGenre(movies):
    movies_pg = movies.copy()
    movies_pg['primaryGenre'] = movies_pg['genres'].apply(first_elem_csv)    
    movies_pg['primaryGenre'] = movies_pg['primaryGenre'].apply(grouppingGenres)
    return movies_pg


def heatmap_6x6(corr_6x6):
    fig = ff.create_annotated_heatmap(corr_6x6.round(2).to_numpy().tolist(),
                x=['Rating de IMDb', 'Metascore', 'Presupuesto', 'Recaudación', 'Beneficio', 'ROI'],
                y=['Rating de IMDb', 'Metascore', 'Presupuesto', 'Recaudación', 'Beneficio', 'ROI'],
                colorscale=[[0, "black"], [1, '#f5c518']],
                font_colors = ['white', 'black'],
                showscale=True,
                zmin=0, zmax=1,
               )

    fig.update_layout(width=800, height=700,  template="plotly_dark")

    fig.update_yaxes(
        autorange="reversed"
    )    

    # Make text size bigger
    for i in range(len(fig.layout.annotations)):
        fig.layout.annotations[i].font.size = 14

    return fig


def heatmap_2x4(corr_2x4):
    fig = ff.create_annotated_heatmap(corr_2x4.round(2).to_numpy().tolist(),
                x=['Presupuesto', 'Recaudación', 'Beneficio', 'ROI'],
                y=['Rating de IMDb', 'Metascore'],
                colorscale=[[0, "black"], [1, '#f5c518']],
                font_colors = ['white'],
                showscale=True,
                zmin=0, zmax=1,
               )

    fig.update_layout(width=800, height=500,  template="plotly_dark"
                    )

    fig.update_xaxes(
        title_text = "Recaudación",
        title_font = {"size": 15},
        title_standoff = 20,
    )

    fig.update_yaxes(
        title_text = "Valoraciones",
        title_font = {"size": 15},
        title_standoff = 20,
        autorange="reversed"
    )    

    # Make text size bigger
    for i in range(len(fig.layout.annotations)):
        fig.layout.annotations[i].font.size = 14

    return fig
