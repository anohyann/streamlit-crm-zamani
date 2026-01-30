# -------------------------------
# Module : Filtre et affichage du DataFrame CRM
# -------------------------------

import streamlit as st
import pandas as pd

def display_dataframe(df):
    # --- Titre principal ---
    st.markdown(
        "<h2 style='color:#2c3e50; font-weight:bold;'>📋 Données CRM filtrables</h2>", 
        unsafe_allow_html=True
    )

    # --- Paramètres de filtres dans la sidebar ---
    st.sidebar.header("🗂️ Filtres du dataset")

    # Choix du mode : filtrer par ligne ou par colonne
    mode_filtre = st.sidebar.radio("Mode de filtre :", ["Par ligne", "Par colonne"])

    colonnes = df.columns.tolist()

    if mode_filtre == "Par ligne":
        # Sélection d'une colonne pour identifier la ligne
        colonne_filtre = st.sidebar.selectbox("Choisir une colonne pour filtrer :", colonnes)
        valeurs_uniques = df[colonne_filtre].dropna().unique().tolist()
        valeur_selectionnee = st.sidebar.selectbox(f"Choisir une valeur dans {colonne_filtre} :", valeurs_uniques)

        # Filtrer la ligne correspondante
        df_filtre = df[df[colonne_filtre] == valeur_selectionnee]

        # Afficher toute la ligne
        st.dataframe(df_filtre, use_container_width=True)

        # Message résumé
        st.info(f"📊 Ligne affichée pour **{colonne_filtre} = {valeur_selectionnee}**")

    else:  # mode "Par colonne"
        # Choisir la colonne à afficher
        colonne_selectionnee = st.sidebar.selectbox("Choisir une colonne à afficher :", colonnes)

        # Afficher uniquement cette colonne
        st.dataframe(df[[colonne_selectionnee]], use_container_width=True)

        # Message résumé
        st.info(f"📊 Colonne affichée : **{colonne_selectionnee}**")