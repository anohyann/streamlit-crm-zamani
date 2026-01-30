import streamlit as st
import plotly.express as px
import pandas as pd

def display_taux_de_conversion_manag(df):
    # --- Copie et création de la variable de conversion ---
    df = df.copy()
    df['conversion'] = df['close_date'].notna().astype(int)

    # --- Agrégation ---
    df_conversion_manager = df.groupby(['manager', 'regional_office']).agg(
        nb_opportunites=('opportunity_id', 'count'),
        nb_conversions=('conversion', 'sum')
    ).reset_index()

    df_conversion_manager['taux_conversion'] = (
        df_conversion_manager['nb_conversions'] / df_conversion_manager['nb_opportunites']
    )

    # --- Titre explicatif ---
    st.markdown(
        "<h3 style='color:#333333; font-weight:bold;'>Taux de conversion par manager et bureau régional</h3>", 
        unsafe_allow_html=True
    )

    # --- Bar chart interactif ---
    fig = px.bar(
        df_conversion_manager,
        x="manager",
        y="taux_conversion",
        color="regional_office",
        barmode="group",
        color_discrete_sequence=px.colors.qualitative.Set2,
        title="Taux de conversion par manager et bureau régional"
    )

    fig.update_layout(
        width=600, height=400,
        plot_bgcolor="#F9F9F9",
        paper_bgcolor="#F9F9F9",
        title_font=dict(size=18, color="#333333", family="Arial"),
        font=dict(size=12, family="Arial"),
        xaxis=dict(title="Manager", tickangle=45),
        yaxis=dict(title="Taux de conversion")
    )

    # --- Affichage du graphique ---
    st.plotly_chart(fig, use_container_width=True)

    # --- Message explicatif ---
    manager_max = df_conversion_manager.sort_values(by='taux_conversion', ascending=False).iloc[0]
    st.markdown(
        f"<p style='text-align:center; color:#444444;'>"
        f"👤 Le manager avec le meilleur taux de conversion est <b>{manager_max['manager']}</b> "
        f"({manager_max['regional_office']}) avec <b>{manager_max['taux_conversion']:.2%}</b>."
        f"</p>", 
        unsafe_allow_html=True
    )