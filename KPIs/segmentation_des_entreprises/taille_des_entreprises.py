import streamlit as st
import plotly.express as px
import pandas as pd

def display_taille_des_entreprises(df):
    # --- Agrégation du chiffre d'affaires par compte ---
    df_ca = df.groupby('account')["close_value"].sum().reset_index(name='chiffre_affaires')

    # --- Tri décroissant et sélection du Top 5 ---
    df_ca = df_ca.sort_values(by="chiffre_affaires", ascending=False).head(5)

    # --- Titre explicatif ---
    st.markdown(
        "<h3 style='color:#333333; font-weight:bold;'>Top 5 comptes par chiffre d'affaires</h3>", 
        unsafe_allow_html=True
    )

    # --- Diagramme en barres horizontales ---
    fig = px.bar(
        df_ca,
        x="chiffre_affaires",
        y="account",
        orientation="h",
        color="chiffre_affaires",
        color_continuous_scale=px.colors.sequential.Blues,
        title="Top 5 comptes par chiffre d'affaires"
    )

    fig.update_layout(
        width=700, height=500,
        plot_bgcolor="#F9F9F9",
        paper_bgcolor="#F9F9F9",
        title_font=dict(size=18, color="#333333", family="Arial"),
        font=dict(size=12, family="Arial"),
        yaxis=dict(title="Compte"),
        xaxis=dict(title="Chiffre d'affaires (USD)")
    )

    # --- Affichage du graphique ---
    st.plotly_chart(fig, use_container_width=True)

    # --- Message résumé ---
    ca_max = df_ca.iloc[0]
    st.markdown(
        f"<p style='text-align:center; color:#444444;'>"
        f"📌 Le compte le plus générateur est <b>{ca_max['account']}</b> "
        f"avec <b>{ca_max['chiffre_affaires']:,}</b> USD."
        f"</p>", 
        unsafe_allow_html=True
    )