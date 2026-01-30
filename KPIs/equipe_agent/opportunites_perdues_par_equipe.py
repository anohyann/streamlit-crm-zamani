import streamlit as st
import plotly.express as px
import pandas as pd

def display_opportunites_perdues_par_equipe(df):
    # --- Création de la variable de perte ---
    df = df.copy()
    df['perdu'] = df['close_date'].isna().astype(int)

    # --- Agrégation par bureau ---
    df_pertes = df.groupby('regional_office')['perdu'].sum().reset_index(name='nb_perdues')

    # --- Titre explicatif ---
    st.markdown(
        "<h3 style='color:#333333; font-weight:bold;'>Opportunités perdues par équipe</h3>", 
        unsafe_allow_html=True
    )

    # --- Graphique bar chart interactif ---
    fig = px.bar(
        df_pertes,
        x="regional_office",
        y="nb_perdues",
        text="nb_perdues",
        color="nb_perdues",
        color_continuous_scale="Reds",
        title="Opportunités perdues par équipe"
    )

    fig.update_traces(textposition="outside")
    fig.update_layout(
        width=600, height=400,
        plot_bgcolor="#F9F9F9",
        paper_bgcolor="#F9F9F9",
        title_font=dict(size=18, color="#333333", family="Arial"),
        font=dict(size=12, family="Arial"),
        xaxis_title="Bureau régional",
        yaxis_title="Nombre d'opportunités perdues"
    )

    # --- Affichage du graphique ---
    st.plotly_chart(fig, use_container_width=True)

    # --- Message résumé ---
    bureau_max = df_pertes.sort_values(by='nb_perdues', ascending=False).iloc[0]
    st.markdown(
        f"<p style='text-align:center; color:#444444;'>"
        f"⚠️ L’équipe ayant perdu le plus d’opportunités est <b>{bureau_max['regional_office']}</b> "
        f"avec <b>{bureau_max['nb_perdues']}</b> cas non conclus."
        f"</p>", 
        unsafe_allow_html=True
    )