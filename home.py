import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import streamlit as st
from PIL import Image


# definition des df a utiliser dans notre page 
df = pd.read_csv("https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv")

# changement nom continent
df['continent'] = df['continent'].replace(' Japan.', 'Japon')
df['continent'] = df['continent'].replace(' Europe.', 'Europe')
df['continent'] = df['continent'].replace(' US.', 'US')

df_jap = df.loc[df['continent'] == 'Japon']
df_euro = df.loc[df['continent'] == 'Europe']
df_us = df.loc[df['continent'] == 'US']

# Intégrer la police Sigmar à Streamlit en utilisant @import
st.markdown("<style>@import url('https://fonts.googleapis.com/css2?family=Carter+One&family=Roboto+Condensed:ital@1&display=swap');</style>", unsafe_allow_html=True)

# image 
image = Image.open('ford.png')


# debut de l'application 

# afficher un titre centrer
st.markdown('<p style="color: #25316D; font-family:Carter One; font-size: 50px; text-align: center;">Le marché mondial de l\'automobile</p>', unsafe_allow_html=True)


# afficher un titre centrer
st.markdown('<p style="color: #25316D; font-family:Carter One; font-size: 45px; text-align: center;">De 1971 à 1983</p>', unsafe_allow_html=True)


# Ajouter un espace
st.markdown("<br><br>", unsafe_allow_html=True)

# afficher un sous titre centrer
st.markdown('<p style="color: #60a9d9; font-family:Carter One; font-size: 35px; text-align: center;">Comparaison entre l\'Europe, le Japon et les US</p>', unsafe_allow_html=True)


# afficher une image
image_container = st.container()
with image_container:
    st.image(image, use_column_width=True)

# Centrer le conteneur
image_container.text_align = "center"

# Ajouter plusieurs espaces
st.markdown("<br><br>", unsafe_allow_html=True)

# afficher un sous titre centrer
st.markdown('<p style="color: #25316D; font-family:Carter One; font-size: 35px; text-align: center; text-decoration: underline;">Corrélations</p>', unsafe_allow_html=True)



# Ajouter plusieurs espaces
st.markdown("<br><br><br>", unsafe_allow_html=True)

# création de la grille horizontale
col1, col2, col3, col4 = st.columns(4)



# Ajouter des styles personnalisés pour les boutons
st.markdown(
    """
    <style>
    .stButton button {
        background-color: #25316D;
        color: #FFFFFF;
        border-color: #60a9d9;
        border-radius: 5px;
        border-width: 2px;
        font-size: 16px;
        font-weight: bold;
        text-transform: uppercase;
    }  
    </style>
    """,
    unsafe_allow_html=True,
)


# Ajouter les boutons à chaque colonne
with col1:
    Global = st.button("Monde")

with col2:
    Europe = st.button("Europe")

with col3:
    Japon = st.button("Japon")

with col4:
    US = st.button('US')
    
# Centrage horizontal des boutons
st.markdown(
    """<style>.stButton { display: flex; justify-content: center; align-items: center;}
    </style>
    """,
    unsafe_allow_html=True,
)
# Ajouter un espace
st.markdown("<br><br>", unsafe_allow_html=True)

# Affichage du contenu en fonction du bouton cliqué
if Global:

    # afficher un sous titre centrer
    st.markdown('<p style="color: #60a9d9; font-family:Carter One; font-size: 25px; text-align: center;text-decoration: underline;">Carte de corrélation Globale</p>',unsafe_allow_html=True)
    # Calculer la matrice de corrélation
    corr_matrix = df.corr()
    # Créer une heatmap avec un dégradé de bleu allant du presque blanc au bleu foncé en cas de corrélation positive
    corr1 = sns.heatmap(corr_matrix.abs(),cmap='Blues', center=0, annot=True, fmt='.2f', annot_kws={"size": 10},vmin=-1, vmax=1)
    # Afficher la figure
    st.pyplot(corr1.figure)
    # Ajouter un espace
    st.markdown("<br>", unsafe_allow_html=True)
    # afficher un texte encadrer
    st.markdown("""<div style='background-color: #f1f1f1; border: 2px solid #777777;border-radius: 5px;padding: 10px; text-align: center; font-family: Arial;'>
        <p>Les données initiales qui comprennent les 3 zones géographiques nous montre que les meilleures corrélations sont entre cylinders et cubicinches (0.95), weightlbs et cubicinches (0.93)  hp et cubicinches (0.91) ainsi qu'entre weightlbs et cylinders (0.89). Globalement, il existe une forte corrélation entre les caractéristiques moteur tel que cylinders, cubicinches, hp ainsi que le poids des véhicules</div>
""", unsafe_allow_html=True)

    
elif Europe:
    
    # afficher un sous titre centrer
    st.markdown('<p style="color: #60a9d9; font-family:Carter One; font-size: 25px; text-align: center;text-decoration: underline;">Carte de corrélation de l\'Europe</p>',unsafe_allow_html=True)
    # Calculer la matrice de corrélation
    corr_euro = df_euro.corr()
    # Créer une heatmap avec un dégradé de bleu allant du presque blanc au bleu foncé en cas de corrélation positive
    corr2 = sns.heatmap(corr_euro.abs(),cmap='Blues', center=0, annot=True, fmt='.2f', annot_kws={"size": 10},vmin=-1, vmax=1)
    #afficher la figure
    st.pyplot(corr2.figure)
     # Ajouter un espace
    st.markdown("<br>", unsafe_allow_html=True)
     # afficher un texte encadrer
    st.markdown("""<div style='background-color: #f1f1f1; border: 2px solid #777777;border-radius: 5px;padding: 10px; text-align: center; font-family: Arial;'>
        <p>Les données de l'Europe nous montre que les meilleures corrélations sont : weightlbs et cubicinches (0.83), puis hp et mpg (0.69) ainsi qu'entre cubicinches et cylinders (0.69). Globalement, il existe les mêmes corrélations que celles du Japon avec une importance en plus pour le rapport consommation/puissance</div>
""", unsafe_allow_html=True)

    
elif Japon:
    
    # afficher un sous titre centrer
    st.markdown('<p style="color: #60a9d9; font-family:Carter One; font-size: 25px; text-align: center;text-decoration: underline;">Carte de corrélation du Japon</p>',unsafe_allow_html=True)
    # Calculer la matrice de corrélation
    corr_jap = df_jap.corr()
    # Créer une heatmap avec un dégradé de bleu allant du presque blanc au bleu foncé en cas de corrélation positive
    corr3 = sns.heatmap(corr_jap.abs(),cmap='Blues', center=0, annot=True, fmt='.2f', annot_kws={"size": 10},vmin=-1, vmax=1)
   # afficher figure
    st.pyplot(corr3.figure)
     # Ajouter un espace
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("""<div style='background-color: #f1f1f1; border: 2px solid #777777;border-radius: 5px;padding: 10px; text-align: center; font-family: Arial;'>
        <p> Les données du Japon nous montre que les meilleures corrélations sont : weightlbs et cubicinches/hp (0.87), puis hp et cubicinches (0.78) ainsi qu'entre cubicinches et cylinders (0.76). Globalement, il existe les mêmes corrélations qu'au niveau mondial avec une importance particulière sur le poids des véhicules, ce qui peut s'expliquer entre autre par le fait que le Japon possède une surface moindre par rapport aux US, les véhicules de petit gabarit semblent donc être majoritaire.</div>
""", unsafe_allow_html=True)
   

    
    
elif US:
    
    # afficher un sous titre centrer
    st.markdown('<p style="color: #60a9d9; font-family:Carter One; font-size: 25px; text-align: center;text-decoration: underline;">Carte de corrélation des US</p>',unsafe_allow_html=True)
    # Calculer la matrice de corrélation
    corr_us = df_us.corr()
    # Créer une heatmap avec un dégradé de bleu allant du presque blanc au bleu foncé en cas de corrélation positive
    corr4 = sns.heatmap(corr_us.abs(),cmap='Blues', center=0, annot=True, fmt='.2f', annot_kws={"size": 10},vmin=-1, vmax=1)
    # afficher figure
    st.pyplot(corr4.figure)
     # Ajouter un espace
    st.markdown("<br>", unsafe_allow_html=True)
    # afficher un sous titre centrer
    st.markdown("""<div style='background-color: #f1f1f1; border: 2px solid #777777;border-radius: 5px;padding: 10px; text-align: center; font-family: Arial;'>
        <p>Les données des US nous montre que les meilleures corrélations sont : cylinders et cubicinches (0.93), cubicinches et weightlbs/hp (0.91) ainsi qu'entre weightlbs et cylinders (0.87). Globalement, il existe les mêmes corrélations qu'au niveau mondial avec les mêmes niveaux de corrélation,  ce qui semble logique, car nous avons beaucoup plus de donnée concernant le marché US que pour les deux autres marchés</div>
""", unsafe_allow_html=True)
    
else:
    # afficher un sous titre centrer
    st.markdown('<p style="color: #60a9d9; font-family:Carter One; font-size: 25px; text-align: center;text-decoration: underline;">Carte de corrélation Globale</p>',unsafe_allow_html=True)
    # Calculer la matrice de corrélation
    corr_matrix = df.corr()
    # Créer une heatmap avec un dégradé de bleu allant du presque blanc au bleu foncé en cas de corrélation positive
    corr1 = sns.heatmap(corr_matrix.abs(),cmap='Blues', center=0, annot=True, fmt='.2f', annot_kws={"size": 10},vmin=-1, vmax=1)
    # Afficher la figure
    st.pyplot(corr1.figure)
    # Ajouter un espace
    st.markdown("<br>", unsafe_allow_html=True)
    # afficher un texte encadrer
    st.markdown("""<div style='background-color: #f1f1f1; border: 2px solid #777777;border-radius: 5px;padding: 10px; text-align: center; font-family: Arial;'>
        <p>Les données initiales comprenant les 3 zones géographiques nous montre que les meilleures corrélations sont entre cylinders et cubicinches (0.95), weightlbs et cubicinches (0.93)  hp et cubicinches (0.91) ainsi qu'entre weightlbs et cylinders (0.89). Globalement, il existe une forte corrélation entre les caractéristiques moteur tel que cylinders, cubicinches, hp ainsi que le poids des véhicules</div>
""", unsafe_allow_html=True)


    
# Ajouter un espace
st.markdown("<br><br>", unsafe_allow_html=True)


 # afficher un sous titre centrer
st.markdown('<p style="color: #25316D; font-family:Carter One; font-size: 35px; text-align: center; text-decoration: underline;">Analyses</p>', unsafe_allow_html=True)



    # Ajouter un espace
st.markdown("<br><br>", unsafe_allow_html=True)

# afficher un sous titre centrer
st.markdown('<p style="color: #60a9d9; font-family:Carter One; font-size: 25px; text-align: center;text-decoration: underline;">Nombre de modèles par an et par continent</p>', unsafe_allow_html=True)

# Grouper les données par année et par pays, puis calculer la taille de chaque groupe
df_count = df.groupby(['year', 'continent']).size().reset_index(name='count')

# Définir un dictionnaire de couleurs pour chaque pays
color_map = {'Europe': '#60a9d9', 'Japon': '#D61C4E', 'US': '#25316D'}

# Créer un histogramme avec la somme du nombre de lignes de chaque pays pour chaque année
fig = px.bar(df_count, x="year", y="count", color="continent", barmode="group",color_discrete_map=color_map)


# Modifier la propriété de l'axe x pour afficher toutes les années
fig.update_layout(xaxis={'type': 'category', 'categoryorder': 'category ascending'})

# Modifier la légende de l'axe X
fig.update_xaxes(title_text="Années")

# Modifier le titre de l'axe y
fig.update_yaxes(title='Nombre de modèles')

# Afficher le graphique
st.plotly_chart(fig)

st.markdown("""<div style='background-color: #f1f1f1; border: 2px solid #777777;border-radius: 5px;padding: 10px; text-align: center; font-family: Arial;'>
        <p>Nous pouvons constater que ce sont les US qui consomment le plus de modèles différents de 71 à 83 hormis en 1981 ou le Japon est en tête. De 1971 à 1977 et en 1980, l'Europe arrive en deuxième position puis le Japon occupe la deuxième place pour les années restantes.</div>
""", unsafe_allow_html=True)



  # Ajouter un espace
st.markdown("<br><br><br>", unsafe_allow_html=True)

# afficher un sous titre centrer
st.markdown('<p style="color: #60a9d9; font-family:Carter One; font-size: 25px; text-align: center;text-decoration: underline;">Puissance moyenne par an et par continent</p>', unsafe_allow_html=True)


# Regrouper les données par année et par continent, puis calculer la consommation maximale de chaque groupe
df_max = df.groupby(['year', 'continent'])['hp'].mean().reset_index(name='hp moyen')

# Définir un dictionnaire de couleurs pour chaque pays
color_map = {'Europe': '#60a9d9', 'Japon': '#D61C4E', 'US': '#25316D'}

# Créer un graphique à barres avec Plotly Express
fig2 = px.bar(df_max, x='year', y='hp moyen', color='continent', barmode="group",color_discrete_map=color_map)

# Modifier la propriété de l'axe x pour afficher toutes les années
fig2.update_layout(xaxis={'type': 'category', 'categoryorder': 'category ascending'})

# Modifier la légende de l'axe X
fig2.update_xaxes(title_text="Années")

# Afficher le graphique
st.plotly_chart(fig2)

st.markdown("""<div style='background-color: #f1f1f1; border: 2px solid #777777;border-radius: 5px;padding: 10px; text-align: center; font-family: Arial;'>
        <p>Nous pouvons constater que les Us sont largement en tête en termes de puissance moyenne de 1971 à 1980, mais cette tendance s'atténue de 1981 à 1983</div>
""", unsafe_allow_html=True)




  # Ajouter un espace
st.markdown("<br><br><br>", unsafe_allow_html=True)

# afficher un sous titre centrer
st.markdown('<p style="color: #60a9d9; font-family:Carter One; font-size: 25px; text-align: center;text-decoration: underline;">Mpg moyen par an et par continent</p>', unsafe_allow_html=True)

# Regrouper les données par année et par continent, puis calculer la consommation maximale de chaque groupe
df_max = df.groupby(['year', 'continent'])['mpg'].mean().reset_index(name='mpg moyen')

# Définir un dictionnaire de couleurs pour chaque pays
color_map = {'Europe': '#60a9d9', 'Japon': '#D61C4E', 'US': '#25316D'}

# Créer un graphique à barres avec Plotly Express
fig3 = px.bar(df_max, x='year', y='mpg moyen', color='continent', barmode="group",color_discrete_map=color_map)

# Modifier la propriété de l'axe x pour afficher toutes les années
fig3.update_layout(xaxis={'type': 'category', 'categoryorder': 'category ascending'})

# Modifier la légende de l'axe X
fig3.update_xaxes(title_text="Années")

# Afficher le graphique
st.plotly_chart(fig3)

st.markdown("""<div style='background-color: #f1f1f1; border: 2px solid #777777;border-radius: 5px;padding: 10px; text-align: center; font-family: Arial;'>
        <p>Nous pouvons constater que le Japon est en tête, suivie de près par l'Europe, alors que les US sont bons derniers chaque année en termes de miles parcourus par gallon d'essence</div>
""", unsafe_allow_html=True)




  # Ajouter un espace
st.markdown("<br><br><br>", unsafe_allow_html=True)

# afficher un sous titre centrer
st.markdown('<p style="color: #60a9d9; font-family:Carter One; font-size: 25px; text-align: center;text-decoration: underline;">Poids moyen par an et par continent</p>', unsafe_allow_html=True)


# Regrouper les données par année et par continent, puis calculer la consommation maximale de chaque groupe
df_max = df.groupby(['year', 'continent'])['weightlbs'].mean().reset_index(name='poids moyen')

# Définir un dictionnaire de couleurs pour chaque pays
color_map = {'Europe': '#60a9d9', 'Japon': '#D61C4E', 'US': '#25316D'}

# Créer un graphique à barres avec Plotly Express
fig4 = px.bar(df_max, x='year', y='poids moyen', color='continent', barmode="group",color_discrete_map=color_map)

# Modifier la propriété de l'axe x pour afficher toutes les années
fig4.update_layout(xaxis={'type': 'category', 'categoryorder': 'category ascending'})

# Modifier la légende de l'axe X
fig4.update_xaxes(title_text="Années")

# Afficher le graphique
st.plotly_chart(fig4)
    
st.markdown("""<div style='background-color: #f1f1f1; border: 2px solid #777777;border-radius: 5px;padding: 10px; text-align: center; font-family: Arial;'>
        <p>Nous pouvons constater que les US sont ceux qui apprécient le plus les voitures avec des gabarits imposants alors que l'Europe et le Japon ont plutôt des véhicules de poids similaire au fil des ans</p>
    </div>
""", unsafe_allow_html=True)


  # Ajouter un espace
st.markdown("<br><br><br>", unsafe_allow_html=True)

# afficher un sous titre centrer
st.markdown('<p style="color: #25316D; font-family:Carter One; font-size: 35px; text-align: center; text-decoration: underline;">Conclusion</p>', unsafe_allow_html=True)


    # Ajouter un espace
st.markdown("<br>", unsafe_allow_html=True)


st.markdown("""<div style='background-color: #f1f1f1; border: 2px solid #777777;border-radius: 5px;padding: 10px; text-align: center; font-family: Arial;'>
        <p>Pour conclure, nous pouvons dire que le continent US est celui qui utilise le plus de modèles différents, généralement des modèles imposant, puissant et qui consomme énormément. Pour ce qui est des marchés japonais et européen, ils sont plutôt similaires, des véhicules de plus petit gabarit, moins puissant, mais qui consomme moins. </p>
    </div>
""", unsafe_allow_html=True)



# legende graph,  git hub , publication 