import streamlit as st
import plotly.express as px
import pandas as pd

def display_comptes_par_secteur(df):
    # --- Agrégation du nombre de comptes par secteur ---
    df_secteur = df.groupby('sector').size().reset_index(name='nb_comptes')
    df_secteur = df_secteur.sort_values(by='nb_comptes', ascending=True)

    # --- Titre explicatif ---
    st.markdown(
        "<h3 style='color:#333333; font-weight:bold;'>Répartition des comptes par secteur</h3>", 
        unsafe_allow_html=True
    )

    # --- Graphique interactif ---
    fig = px.bar(
        df_secteur,
        x="nb_comptes",
        y="sector",
        orientation="h",
        color="nb_comptes",
        color_continuous_scale=["#1E90FF", "#32CD32"],  # Bleu → Vert
        title="Répartition des comptes par secteur"
    )

    fig.update_layout(
        width=600, height=400,
        plot_bgcolor="#F9F9F9",
        paper_bgcolor="#F9F9F9",
        title_font=dict(size=18, color="#333333", family="Arial"),
        font=dict(size=12, family="Arial")
    )

    # --- Affichage du graphique ---
    st.plotly_chart(fig, use_container_width=True)

    # --- Message résumé ---
    secteur_max = df_secteur.sort_values(by='nb_comptes', ascending=False).iloc[0]
    st.markdown(
        f"<p style='text-align:center; color:#444444;'>"
        f"✅ Le secteur dominant est <b>{secteur_max['sector']}</b> "
        f"avec <b>{secteur_max['nb_comptes']}</b> comptes enregistrés."
        f"</p>", 
        unsafe_allow_html=True
    )