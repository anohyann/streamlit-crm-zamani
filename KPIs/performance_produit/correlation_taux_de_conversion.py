import streamlit as st
import plotly.express as px
import pandas as pd

def display_correlation_taux_de_conversion(df):
    # --- Création de la variable binaire de conversion ---
    df = df.copy()
    df['conversion'] = df['close_date'].notna().astype(int)

    # --- Titre explicatif ---
    st.markdown(
        "<h3 style='color:#333333; font-weight:bold;'>Corrélation entre prix de vente et probabilité de conversion</h3>", 
        unsafe_allow_html=True
    )

    # --- Scatter plot interactif ---
    fig = px.scatter(
        df,
        x="sales_price",
        y="conversion",
        color="conversion",
        color_discrete_map={0: "#FF8C00", 1: "#32CD32"},  # Orange pour non converti, vert pour converti
        opacity=0.6,
        title="Corrélation entre prix et conversion"
    )

    fig.update_layout(
        width=600, height=400,
        plot_bgcolor="#F9F9F9",
        paper_bgcolor="#F9F9F9",
        title_font=dict(size=18, color="#333333", family="Arial"),
        font=dict(size=12, family="Arial"),
        xaxis=dict(title="Prix de vente"),
        yaxis=dict(title="Probabilité de conversion")
    )

    # --- Affichage du graphique ---
    st.plotly_chart(fig, use_container_width=True)

    # --- Calcul de la corrélation ---
    corr = df[['sales_price', 'conversion']].corr().iloc[0, 1]
    relation = "positive" if corr > 0 else "négative" if corr < 0 else "nulle"

    # --- Message résumé ---
    st.markdown(
        f"<p style='text-align:center; color:#444444;'>"
        f"📈 La corrélation entre le prix de vente et la conversion est de <b>{corr:.2f}</b>, "
        f"ce qui indique une relation <b>{relation}</b>."
        f"</p>", 
        unsafe_allow_html=True
    )