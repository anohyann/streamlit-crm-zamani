import streamlit as st
import plotly.express as px
import pandas as pd

def display_part_filiale_societe_mere(df):
    # --- Nettoyage de la colonne is_subsidiary ---
    df = df.copy()
    df['is_subsidiary'] = df['is_subsidiary'].astype(str).str.strip().str.title()

    # --- Agrégation ---
    df_filiales = df.groupby('is_subsidiary').size().reset_index(name='nb_comptes')

    # --- Titre explicatif ---
    st.markdown(
        "<h3 style='color:#333333; font-weight:bold;'>Répartition des comptes : Filiales vs Maisons mères</h3>", 
        unsafe_allow_html=True
    )

    # --- Treemap interactif ---
    fig = px.treemap(
        df_filiales,
        path=['is_subsidiary'],
        values='nb_comptes',
        color='nb_comptes',
        color_continuous_scale=["#1E90FF", "#32CD32"],  # Bleu → Vert
        title="Répartition des comptes : Filiales vs Maisons mères"
    )

    fig.update_layout(
        width=600, height=400,
        margin=dict(t=50, l=25, r=25, b=25),
        plot_bgcolor="#F9F9F9",
        paper_bgcolor="#F9F9F9",
        title_font=dict(size=18, color="#333333", family="Arial"),
        font=dict(size=12, family="Arial")
    )

    # --- Affichage du graphique ---
    st.plotly_chart(fig, use_container_width=True)

    # --- Message résumé ---
    type_max = df_filiales.sort_values(by='nb_comptes', ascending=False).iloc[0]
    st.markdown(
        f"<p style='text-align:center; color:#444444;'>"
        f"🏢 L’entité la plus représentée est <b>{type_max['is_subsidiary']}</b> "
        f"avec <b>{type_max['nb_comptes']}</b> comptes."
        f"</p>", 
        unsafe_allow_html=True
    )