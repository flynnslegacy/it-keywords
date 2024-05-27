import streamlit as st
import pandas as pd

# Charger les données
file_path = 'dictionnaire-ensitech.xlsx'
datas_brutes_df = pd.read_excel(file_path, sheet_name='datas-brutes')
definitions_df = pd.read_excel(file_path, sheet_name='definitions')

# Extraire les mots clés uniques
keywords = pd.concat([datas_brutes_df['Mot Clés'], definitions_df['Mot Clés']]).dropna().unique()
keywords = [''] + list(keywords)  # Ajouter une option vide


# Fonction pour obtenir les informations par mot-clé
def get_info_by_keyword(keyword):
    definition = definitions_df[definitions_df['Mot Clés'].str.contains(keyword, case=False, na=False)]
    related_data = datas_brutes_df[datas_brutes_df['Mot Clés'].str.contains(keyword, case=False, na=False)]
    
    if not definition.empty:
        definition_text = definition.iloc[0]['Définitions']
    else:
        definition_text = 'Définition non trouvée.'
    
    formations = related_data['Formations'].dropna().unique().tolist()
    metiers = related_data['Métiers'].dropna().unique().tolist()
    competences = related_data['Compétences'].dropna().unique().tolist()
    
    return definition_text, formations, metiers, competences

# Interface utilisateur
st.title('Dictionnaire ENSITECH')

# Utiliser un selectbox pour l'autofill des mots clés
keyword = st.selectbox('Entrez ou sélectionnez un mot-clé :', options=keywords)

if keyword:
    definition, formations, metiers, competences = get_info_by_keyword(keyword)
    
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
