import streamlit as st
import pandas as pd

# Charger les données
file_path = 'dictionnaire-ensitech.xlsx'
datas_brutes_df = pd.read_excel(file_path, sheet_name='datas-brutes')
definitions_df = pd.read_excel(file_path, sheet_name='definitions')

# Extraire les mots clés uniques
keywords = pd.concat([datas_brutes_df['Mot Clés'], definitions_df['Mot Clés']]).dropna().unique()
formations = datas_brutes_df['Formations'].dropna().unique()
metiers = datas_brutes_df['Métiers'].dropna().unique()
competences = datas_brutes_df['Compétences'].dropna().unique()

# Ajouter une option vide
keywords = [''] + list(keywords)
formations = [''] + list(formations)
metiers = [''] + list(metiers)
competences = [''] + list(competences)

# Fonction pour obtenir les informations par catégorie
def get_info_by_category(category, value):
    if category == 'Mot Clé':
        related_data = datas_brutes_df[datas_brutes_df['Mot Clés'].str.contains(value, case=False, na=False)]
        definition = definitions_df[definitions_df['Mot Clés'].str.contains(value, case=False, na=False)]
        if not definition.empty:
            definition_text = definition.iloc[0]['Définitions']
        else:
            definition_text = 'Définition non trouvée.'
    elif category == 'Formation':
        related_data = datas_brutes_df[datas_brutes_df['Formations'].str.contains(value, case=False, na=False)]
        definition_text = 'Définition non disponible pour cette recherche.'
    elif category == 'Métier':
        related_data = datas_brutes_df[datas_brutes_df['Métiers'].str.contains(value, case=False, na=False)]
        definition_text = 'Définition non disponible pour cette recherche.'
    elif category == 'Compétence':
        related_data = datas_brutes_df[datas_brutes_df['Compétences'].str.contains(value, case=False, na=False)]
        definition_text = 'Définition non disponible pour cette recherche.'

    formations = related_data['Formations'].dropna().unique().tolist()
    metiers = related_data['Métiers'].dropna().unique().tolist()
    competences = related_data['Compétences'].dropna().unique().tolist()
    
    return definition_text, formations, metiers, competences

# Interface utilisateur
st.title('Dictionnaire EnsiTech')

# Sélection de la catégorie de recherche avec une option vide
category = st.selectbox('Choisissez une catégorie de recherche :', ['', 'Mot Clé', 'Formation', 'Métier', 'Compétence'])

# Sélection de la valeur en fonction de la catégorie
value = None
if category == 'Mot Clé':
    value = st.selectbox('Entrez ou sélectionnez un mot-clé :', options=keywords)
elif category == 'Formation':
    value = st.selectbox('Entrez ou sélectionnez une formation :', options=formations)
elif category == 'Métier':
    value = st.selectbox('Entrez ou sélectionnez un métier :', options=metiers)
elif category == 'Compétence':
    value = st.selectbox('Entrez ou sélectionnez une compétence :', options=competences)

# Affichage des résultats
if value and value != '':
    definition, formations, metiers, competences = get_info_by_category(category, value)
    
    if category == 'Mot Clé':
        st.subheader('Définition')
        st.write(definition)
    
    st.subheader('Formations')
    for formation in formations:
        st.write(f"- {formation}")
    
    st.subheader('Métiers')
    for metier in metiers:
        st.write(f"- {metier}")
    
    st.subheader('Compétences')
    for competence in competences:
        st.write(f"- {competence}")

# Pour exécuter l'application, utilisez la commande suivante dans le terminal:
# streamlit run app.py
