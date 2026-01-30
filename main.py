import streamlit as st
import pandas as pd

# Import des modules de KPIs
from KPIs.segmentation_des_entreprises import (
    comptes_par_secteur,
    taille_des_entreprises,
    part_filiale_societe_mere
)

from KPIs.performance_produit import (
    CA_par_produit,
    CA_par_gamme_de_produit,
    prix_moyen_par_produit,
    taux_de_conversion_opp,
    correlation_taux_de_conversion
)

from KPIs.cycle_de_vente import (
    taux_de_conversion_glob,
    duree_moyenne,
    taux_de_chute_opp,
    valeur_moyenne
)

from KPIs.equipe_agent import (
    CA_par_region,
    taux_de_conversion_manag,
    volume_de_ventes_par_agent,
    opportunites_perdues_par_equipe
)

# -------------------------------
# Configuration de la page
# -------------------------------
st.set_page_config(
    page_title="CRM Dashboard",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -------------------------------
# Chargement des données
# -------------------------------
@st.cache_data
def load_data():
    return pd.read_csv("C:/Users/USER/stream_lab/datasets/crm_final_clean_tb.csv")

df = load_data()

# -------------------------------
# Sidebar - logo entreprise
# -------------------------------
st.sidebar.image(
    r"C:/Users/USER/stream_lab/assets/zamani.jpg",
    width=180  # taille moyenne, ajuste si besoin
)

# -------------------------------
# Sidebar - filtres globaux
# -------------------------------
st.sidebar.markdown(
    """
    <div style="
        background-color:#f8f9fa;
        padding:15px;
        border-radius:10px;
        border:1px solid #ddd;
    ">
    <h3 style="color:#2c3e50;">🔎Centre de filtres CRM
</h3>
    """,
    unsafe_allow_html=True
)

categorie = st.sidebar.selectbox(
    "Choisir une catégorie d’analyse :",
    ["Segmentation entreprise", "Performance produit", "Cycle de vente", "Équipe & Agents"]
)

st.sidebar.markdown("---")
st.sidebar.write("📊 Données CRM nettoyées et agrégées")
st.sidebar.markdown("</div>", unsafe_allow_html=True)

# -------------------------------
# Corps du Dashboard
# -------------------------------
st.markdown(
    """
    <h1 style='text-align: center; font-size: 60px; color: #2c3e50; margin-bottom:30px;'>
        📊 TABLEAU DE BORD CRM INTERACTIF
    </h1>
    <hr style="border:1px solid #ddd; margin-bottom:40px;">
    """,
    unsafe_allow_html=True
)

# -------------------------------
# Catégorie 1 : Segmentation entreprise
# -------------------------------
if categorie == "Segmentation entreprise":
    st.markdown("<h2 style='text-align:center;font-weight:bold;font-size:40px;'>🏢 Segmentation des entreprises</h2>", unsafe_allow_html=True)

    col1, col2 = st.columns([1,1], gap="large")
    with col1:
        comptes_par_secteur.display_comptes_par_secteur(df)
    with col2:
        taille_des_entreprises.display_taille_des_entreprises(df)

    st.divider()
    part_filiale_societe_mere.display_part_filiale_societe_mere(df)

# -------------------------------
# Catégorie 2 : Performance produit
# -------------------------------
elif categorie == "Performance produit":
    st.markdown("<h2 style='text-align:center;font-weight:bold;font-size:40px;'>📦 Performance des produits</h2>", unsafe_allow_html=True)

    col1, col2 = st.columns([1,1], gap="large")
    with col1:
        CA_par_produit.display_CA_par_produit(df)
    with col2:
        CA_par_gamme_de_produit.display_CA_par_gamme_de_produit(df)

    st.divider()
    col3, col4 = st.columns([1,1], gap="large")
    with col3:
        prix_moyen_par_produit.display_prix_moyen_par_produit(df)
    with col4:
        taux_de_conversion_opp.display_taux_de_conversion_opp(df)

    st.divider()
    correlation_taux_de_conversion.display_correlation_taux_de_conversion(df)

# -------------------------------
# Catégorie 3 : Cycle de vente
# -------------------------------
elif categorie == "Cycle de vente":
    st.markdown("<h2 style='text-align:center;font-weight:bold;font-size:40px;'>⏱️ Cycle de vente</h2>", unsafe_allow_html=True)

    col1, col2 = st.columns([1,1], gap="large")
    with col1:
        taux_de_conversion_glob.display_taux_de_conversion_glob(df)
    with col2:
        duree_moyenne.display_duree_moyenne(df)

    st.divider()
    col3, col4 = st.columns([1,1], gap="large")
    with col3:
        taux_de_chute_opp.display_taux_de_chute_opp(df)
    with col4:
        valeur_moyenne.display_valeur_moyenne(df)

# -------------------------------
# Catégorie 4 : Équipe & Agents
# -------------------------------
elif categorie == "Équipe & Agents":
    st.markdown("<h2 style='text-align:center;font-weight:bold;font-size:40px;'>👥 Équipe & Agents</h2>", unsafe_allow_html=True)

    col1, col2 = st.columns([1,1], gap="large")
    with col1:
        CA_par_region.display_CA_par_region(df)
    with col2:
        taux_de_conversion_manag.display_taux_de_conversion_manag(df)

    st.divider()
    col3, col4 = st.columns([1,1], gap="large")
    with col3:
        volume_de_ventes_par_agent.display_volume_de_ventes_par_agent(df)
    with col4:
        opportunites_perdues_par_equipe.display_opportunites_perdues_par_equipe(df)

    # --- Section : Affichage du DataFrame CRM avec filtre ---
import pandas as pd
from KPIs import filtre_dataframe

# Chargement du DataFrame CRM depuis ton fichier CSV
crm_final_clean_tb = pd.read_csv(
    r"C:/Users/USER/stream_lab/datasets/crm_final_clean_tb.csv"
)

# Appel de la fonction d’affichage avec filtre
filtre_dataframe.display_dataframe(crm_final_clean_tb)

