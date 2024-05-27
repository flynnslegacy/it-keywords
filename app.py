import streamlit as st
import pandas as pd

# Charger les données
xls = pd.ExcelFile('./dictionnaire-ensitech.xlsx')
datas_brutes_df = pd.read_excel(xls, sheet_name='datas-brutes')
definitions_df = pd.read_excel(xls, sheet_name='definitions')

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
st.title('Dictionnaire EnsiTech')

keyword = st.text_input('Entrez un mot-clé :')

if keyword:
    definition, formations, metiers, competences = get_info_by_keyword(keyword)
    
    st.subheader('Définition')
    st.write(definition)
    
    st.subheader('Formations')
    st.write(', '.join(formations))
    
    st.subheader('Métiers')
    st.write(', '.join(metiers))
    
    st.subheader('Compétences')
    st.write(', '.join(competences))

# Pour exécuter l'application, utilisez la commande suivante dans le terminal:
# streamlit run app.py
