import streamlit as st
import plotly.express as px
import pandas as pd

def display_prix_moyen_par_produit(df):
    # --- Nettoyage éventuel des valeurs nulles ---
    df_box = df.dropna(subset=['sales_price', 'product'])

    # --- Titre explicatif ---
    st.markdown(
        "<h3 style='color:#333333; font-weight:bold;'>Distribution des prix par produit</h3>", 
        unsafe_allow_html=True
    )

    # --- Boxplot interactif ---
    fig = px.box(
        df_box,
        x="product",
        y="sales_price",
        color="product",
        color_discrete_sequence=px.colors.qualitative.Pastel,  # Palette douce
        title="Distribution des prix par produit"
    )

    fig.update_layout(
        width=600, height=400,
        plot_bgcolor="#F9F9F9",
        paper_bgcolor="#F9F9F9",
        title_font=dict(size=18, color="#333333", family="Arial"),
        font=dict(size=12, family="Arial"),
        xaxis=dict(title="Produit", tickangle=45),
        yaxis=dict(title="Prix de vente (USD)")
    )

    # --- Affichage du graphique ---
    st.plotly_chart(fig, use_container_width=True)

    # --- Calcul du prix moyen par produit ---
    df_moyen = df_box.groupby('product')['sales_price'].mean().reset_index()
    produit_max = df_moyen.sort_values(by='sales_price', ascending=False).iloc[0]

    # --- Message résumé ---
    st.markdown(
        f"<p style='text-align:center; color:#444444;'>"
        f"💸 Le produit avec le prix moyen le plus élevé est <b>{produit_max['product']}</b> "
        f"avec <b>{produit_max['sales_price']:.2f} USD</b> en moyenne."
        f"</p>", 
        unsafe_allow_html=True
    )