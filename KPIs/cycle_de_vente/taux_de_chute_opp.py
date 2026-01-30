import streamlit as st
import plotly.express as px
import pandas as pd

def display_taux_de_chute_opp(df):
    # --- Comptage des opportunités par étape ---
    df_funnel = df.groupby('deal_stage').size().reset_index(name='nb_opportunites')

    # --- Tri des étapes (par volume décroissant si ordre logique inconnu) ---
    df_funnel = df_funnel.sort_values(by='nb_opportunites', ascending=False)

    # --- Titre explicatif ---
    st.markdown(
        "<h3 style='color:#333333; font-weight:bold;'>Taux de chute par étape du cycle de vente</h3>", 
        unsafe_allow_html=True
    )

# --- Funnel chart interactif ---
    fig = px.funnel(
    df_funnel,
    x="nb_opportunites",
    y="deal_stage",
    title="Taux de chute par étape du cycle de vente",
    color="deal_stage",  # on colore par étape plutôt que par valeur
    color_discrete_sequence=["#FF8C00", "#6A5ACD"] # Orange → Violet cohérent avec cycle de vente
    ) 
    fig.update_layout(
        width=600, height=400,
        margin=dict(t=50, l=25, r=25, b=25),
        plot_bgcolor="#F9F9F9",
        paper_bgcolor="#F9F9F9",
        title_font=dict(size=18, color="#333333", family="Arial"),
        font=dict(size=12, family="Arial")
    )

    # --- Affichage du graphique ---
    st.plotly_chart(fig, use_container_width=True)

    # --- Message résumé ---
    etape_max = df_funnel.iloc[0]
    etape_min = df_funnel.iloc[-1]
    st.markdown(
        f"<p style='text-align:center; color:#444444;'>"
        f"🔁 L’étape la plus chargée est <b>{etape_max['deal_stage']}</b> "
        f"avec <b>{etape_max['nb_opportunites']}</b> opportunités, "
        f"tandis que l’étape la plus faible est <b>{etape_min['deal_stage']}</b> "
        f"avec <b>{etape_min['nb_opportunites']}</b>."
        f"</p>", 
        unsafe_allow_html=True
    )