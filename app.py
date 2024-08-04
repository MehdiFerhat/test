import streamlit as st

# Titre de l'application
st.title("Calculateur interactif")

# Curseurs et entrées
taxe_vendeur = st.slider("Taxe Vendeur (%)", 0, 100) / 100
cout_km_client = st.number_input("Coût KM Client", min_value=0.0, max_value=10.0, value=0.0, step=0.1)
cout_kg_client = st.number_input("Coût KG Client", min_value=0.0, max_value=10.0, value=0.0, step=0.1)
nb_kilometres = st.number_input("Nombre de Kilomètres", min_value=0, value=0, step=1)
cout_fixe = st.number_input("Coût Fixe", min_value=0.0, value=0.0, step=0.1)
cout_km_concu = st.number_input("Coût KM Concu", min_value=0.0, value=0.0, step=0.1)

# Calculs
result = 10 * taxe_vendeur + cout_km_client * nb_kilometres + cout_kg_client
required = cout_fixe + cout_km_concu * nb_kilometres
benefice = result - required

# Affichage des résultats
st.write(f"Résultat : {result:.2f}")
st.write(f"Valeur requise : {required:.2f}")
st.write(f"Bénéfice possible : {benefice:.2f}")
