import streamlit as st
import plotly.express as px
import pandas as pd

def display_CA_par_produit(df):
    # --- Agrégation du CA par produit ---
    df_ca_produit = df.groupby('product')['close_value'].sum().reset_index()

    # --- Tri décroissant ---
    df_ca_produit = df_ca_produit.sort_values(by='close_value', ascending=False)

    # --- Titre explicatif ---
    st.markdown(
        "<h3 style='color:#333333; font-weight:bold;'>Chiffre d’affaires par produit</h3>", 
        unsafe_allow_html=True
    )

    # --- Bar chart interactif ---
    fig = px.bar(
        df_ca_produit,
        x="product",
        y="close_value",
        color="close_value",
        color_continuous_scale=["#FF8C00", "#6A5ACD"],  # Orange → Violet pour la catégorie performance produit
        title="Chiffre d’affaires par produit"
    )

    fig.update_layout(
        width=600, height=400,
        plot_bgcolor="#F9F9F9",
        paper_bgcolor="#F9F9F9",
        title_font=dict(size=18, color="#333333", family="Arial"),
        font=dict(size=12, family="Arial"),
        xaxis=dict(title="Produit", tickangle=45),
        yaxis=dict(title="Chiffre d’affaires (USD)")
    )

    # --- Affichage du graphique ---
    st.plotly_chart(fig, use_container_width=True)

    # --- Message résumé ---
    produit_max = df_ca_produit.iloc[0]
    st.markdown(
        f"<p style='text-align:center; color:#444444;'>"
        f"💰 Le produit le plus générateur de chiffre d’affaires est <b>{produit_max['product']}</b> "
        f"avec un total de <b>{produit_max['close_value']:.2f} USD</b>."
        f"</p>", 
        unsafe_allow_html=True
    )