import streamlit as st
import plotly.express as px
import pandas as pd

def display_taux_de_conversion_glob(df):
    # --- Création de la variable binaire de conversion ---
    df = df.copy()
    df['conversion'] = df['close_date'].notna().astype(int)

    # --- Agrégation ---
    total_opportunites = df.shape[0]
    total_conversions = df['conversion'].sum()
    taux_conversion_global = total_conversions / total_opportunites

    # --- Titre explicatif ---
    st.markdown(
        "<h3 style='color:#333333; font-weight:bold;'>Taux de conversion global</h3>", 
        unsafe_allow_html=True
    )

    # --- Bar chart interactif ---
    df_global = pd.DataFrame({
        "Type": ["Conversion"],
        "Taux": [taux_conversion_global]
    })

    fig = px.bar(
        df_global,
        x="Type",
        y="Taux",
        color="Taux",
        color_continuous_scale=["#FF8C00", "#6A5ACD"],  # Orange → Violet cohérent avec cycle de vente
        title="Taux de conversion global"
    )

    fig.update_layout(
        width=600, height=400,
        plot_bgcolor="#F9F9F9",
        paper_bgcolor="#F9F9F9",
        title_font=dict(size=18, color="#333333", family="Arial"),
        font=dict(size=12, family="Arial"),
        yaxis=dict(range=[0, 1], title="Taux de conversion")
    )

    # --- Affichage du graphique ---
    st.plotly_chart(fig, use_container_width=True)

    # --- Message résumé ---
    st.markdown(
        f"<p style='text-align:center; color:#444444;'>"
        f"📊 Le taux de conversion global est de <b>{taux_conversion_global:.2%}</b>, "
        f"soit <b>{total_conversions}</b> opportunités conclues sur <b>{total_opportunites}</b>."
        f"</p>", 
        unsafe_allow_html=True
    )