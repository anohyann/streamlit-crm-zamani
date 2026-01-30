import streamlit as st
import plotly.express as px
import pandas as pd

def display_CA_par_region(df):
    # --- Agrégation du CA par bureau régional ---
    df_ca_bureau = df.groupby('regional_office')['close_value'].sum().reset_index()

    # --- Tri décroissant ---
    df_ca_bureau = df_ca_bureau.sort_values(by='close_value', ascending=False)

    # --- Titre explicatif ---
    st.markdown(
        "<h3 style='color:#333333; font-weight:bold;'>Chiffre d’affaires par bureau régional</h3>", 
        unsafe_allow_html=True
    )

    # --- Bar chart interactif ---
    fig = px.bar(
        df_ca_bureau,
        x="regional_office",
        y="close_value",
        color="close_value",
        color_continuous_scale=["#1E90FF", "#32CD32"],  # Bleu → Vert pour cohérence équipe/agent
        title="Chiffre d’affaires par bureau régional"
    )

    fig.update_layout(
        width=600, height=400,
        plot_bgcolor="#F9F9F9",
        paper_bgcolor="#F9F9F9",
        title_font=dict(size=18, color="#333333", family="Arial"),
        font=dict(size=12, family="Arial"),
        xaxis=dict(title="Bureau régional", tickangle=45),
        yaxis=dict(title="Chiffre d’affaires (USD)")
    )

    # --- Affichage du graphique ---
    st.plotly_chart(fig, use_container_width=True)

    # --- Message résumé ---
    bureau_max = df_ca_bureau.iloc[0]
    st.info(f"🏢 Le bureau régional le plus performant est **{bureau_max['regional_office']}** "
    f"avec un chiffre d’affaires total de **{bureau_max['close_value']:.2f} USD**."
    )