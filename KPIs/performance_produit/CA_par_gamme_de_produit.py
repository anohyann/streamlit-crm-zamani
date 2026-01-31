import streamlit as st
import plotly.express as px
import pandas as pd

def display_CA_par_gamme_de_produit(df):
    # --- Nettoyage des libellés ---
    df['series'] = df['series'].str.strip().str.upper()
    gammes_valides = ["GTK", "GTX", "MG"]
    df = df[df['series'].isin(gammes_valides)]

    # --- Agrégation du CA par produit et série ---
    df_ca_gamme = df.groupby(['series', 'product'])['close_value'].sum().reset_index()

    # --- Titre explicatif ---
    st.subheader("💰 Chiffre d’affaires par gamme et produit")

    # --- Bar chart groupé interactif ---
    fig = px.bar(
        df_ca_gamme,
        x="product",
        y="close_value",
        color="series",
        barmode="group",
        color_discrete_sequence=px.colors.qualitative.Set2,
        title="Chiffre d’affaires par gamme et produit"
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
    gamme_max = (
        df_ca_gamme.groupby('series')['close_value']
        .sum()
        .reset_index()
        .sort_values(by='close_value', ascending=False)
        .iloc[0]
    )
    st.markdown(
        f"<p style='text-align:center; color:#444444;'>"
        f"🏷️ La gamme la plus performante est <b>{gamme_max['series']}</b> "
        f"avec un chiffre d’affaires total de <b>{gamme_max['close_value']:.2f} USD</b>."
        f"</p>", 
        unsafe_allow_html=True
    )