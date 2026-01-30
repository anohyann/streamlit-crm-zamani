import streamlit as st
import plotly.express as px
import pandas as pd

def display_valeur_moyenne(df):
    # --- Filtrer les opportunités gagnées ---
    df_gagnees = df.dropna(subset=['close_date'])

    # --- Agrégation de la valeur moyenne par produit ---
    df_valeur = df_gagnees.groupby('product')['close_value'].mean().reset_index()

    # --- Tri décroissant ---
    df_valeur = df_valeur.sort_values(by='close_value', ascending=False)

    # --- Titre explicatif ---
    st.markdown(
        "<h3 style='color:#333333; font-weight:bold;'>Valeur moyenne des opportunités gagnées par produit</h3>", 
        unsafe_allow_html=True
    )

    # --- Bar chart interactif ---
    fig = px.bar(
        df_valeur,
        x="product",
        y="close_value",
        color="close_value",
        color_continuous_scale=["#32CD32", "#006400"],  # Vert clair → vert foncé cohérent avec cycle de vente
        title="Valeur moyenne des opportunités gagnées par produit"
    )

    fig.update_layout(
        width=600, height=400,
        plot_bgcolor="#F9F9F9",
        paper_bgcolor="#F9F9F9",
        title_font=dict(size=18, color="#333333", family="Arial"),
        font=dict(size=12, family="Arial"),
        xaxis=dict(title="Produit", tickangle=45),
        yaxis=dict(title="Valeur moyenne (USD)")
    )

    # --- Affichage du graphique ---
    st.plotly_chart(fig, use_container_width=True)

    # --- Message résumé ---
    produit_max = df_valeur.iloc[0]
    st.markdown(
        f"<p style='text-align:center; color:#444444;'>"
        f"🏆 Le produit avec la valeur moyenne la plus élevée parmi les opportunités gagnées est "
        f"<b>{produit_max['product']}</b> avec <b>{produit_max['close_value']:.2f} USD</b>."
        f"</p>", 
        unsafe_allow_html=True
    )