import streamlit as st
import plotly.express as px
import pandas as pd
import datetime as dt

def display_duree_moyenne(df):
    # --- Copie de sécurité ---
    df = df.copy()

    # --- Filtrer les mois valides (1 à 12) ---
    df = df[df['mois_vente'].between(1, 12)]

    # --- Conversion en nom de mois ---
    df['mois_vente'] = df['mois_vente'].apply(lambda x: dt.date(1900, int(x), 1).strftime('%B'))

    # --- Ordre chronologique ---
    mois_ordre = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]
    df['mois_vente'] = pd.Categorical(df['mois_vente'], categories=mois_ordre, ordered=True)

    # --- Agrégation ---
    df_cycle = df.groupby('mois_vente')['cycle_vente_jours'].mean().reset_index()
    df_cycle = df_cycle.sort_values(by='mois_vente')

    # --- Titre explicatif ---
    st.markdown(
        "<h3 style='color:#333333; font-weight:bold;'>📊 Durée moyenne du cycle de vente par mois</h3>", 
        unsafe_allow_html=True
    )

    # --- Calcul de la durée moyenne globale ---
    duree_moyenne = df['cycle_vente_jours'].mean()
    st.markdown(
        f"<p style='text-align:center; color:#444444;'>"
        f"⏱️ La durée moyenne du cycle de vente est de <b>{duree_moyenne:.1f} jours</b> "
        f"sur l’ensemble des opportunités."
        f"</p>", 
        unsafe_allow_html=True
    )

    # --- Courbe interactive avec Plotly ---
    fig = px.line(
        df_cycle,
        x="mois_vente",
        y="cycle_vente_jours",
        markers=True,
        title="Durée moyenne du cycle de vente par mois",
        labels={"mois_vente": "Mois de vente", "cycle_vente_jours": "Durée moyenne (jours)"},
        line_shape="linear",
        color_discrete_sequence=["#FF8C00"]  # Orange cohérent avec cycle de vente
    )

    fig.update_layout(
        width=600, height=400,
        plot_bgcolor="#F9F9F9",
        paper_bgcolor="#F9F9F9",
        title_font=dict(size=18, color="#333333", family="Arial"),
        font=dict(size=12, family="Arial"),
        xaxis=dict(tickangle=-45)
    )

    # --- Affichage du graphique ---
    st.plotly_chart(fig, use_container_width=True)