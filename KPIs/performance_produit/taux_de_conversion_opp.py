import streamlit as st
import plotly.express as px
import pandas as pd

def display_taux_de_conversion_opp(df):
    # --- Nettoyage des libellés ---
    df['series'] = df['series'].str.strip().str.upper()
    gammes_valides = ["GTK", "GTX", "MG"]
    df = df[df['series'].isin(gammes_valides)]

    # --- Calcul du taux de conversion par gamme ---
    df_conversion = df.groupby('series').agg(
        nb_opportunites=('opportunity_id', 'count'),
        nb_closures=('close_date', 'count')
    ).reset_index()

    if df_conversion.empty:
        st.warning("⚠️ Aucune donnée disponible pour les gammes sélectionnées.")
        return

    df_conversion['taux_conversion'] = df_conversion['nb_closures'] / df_conversion['nb_opportunites']

    # --- Tri décroissant ---
    df_conversion = df_conversion.sort_values(by='taux_conversion', ascending=False)

    # --- Titre explicatif ---
    st.subheader("🎯 Taux de conversion par gamme")

    # --- Bar chart interactif ---
    fig = px.bar(
        df_conversion,
        x="series",
        y="taux_conversion",
        color="taux_conversion",
        color_continuous_scale=["#FF8C00", "#6A5ACD"],
        title="Taux de conversion par gamme"
    )

    fig.update_layout(
        width=600, height=400,
        plot_bgcolor="#F9F9F9",
        paper_bgcolor="#F9F9F9",
        title_font=dict(size=18, color="#333333", family="Arial"),
        font=dict(size=12, family="Arial"),
        xaxis=dict(title="Gamme", tickangle=45),
        yaxis=dict(title="Taux de conversion")
    )

    st.plotly_chart(fig, use_container_width=True)

    # --- Message résumé ---
    if not df_conversion.empty:
        gamme_max = df_conversion.iloc[0]
        st.markdown(
            f"<p style='text-align:center; color:#444444;'>"
            f"🏆 La gamme avec le meilleur taux de conversion est <b>{gamme_max['series']}</b> "
            f"avec <b>{gamme_max['taux_conversion']:.2%}</b>."
            f"</p>", 
            unsafe_allow_html=True
        )