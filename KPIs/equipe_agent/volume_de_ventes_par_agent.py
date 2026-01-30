import streamlit as st
import plotly.express as px
import pandas as pd

def display_volume_de_ventes_par_agent(df):
    # --- Agrégation par agent ---
    df_volume = df.groupby('sales_agent')['opportunity_id'].count().reset_index(name='nb_ventes')

    # --- Titre explicatif ---
    st.markdown(
        "<h3 style='color:#333333; font-weight:bold;'>Volume de ventes par agent</h3>", 
        unsafe_allow_html=True
    )

    # --- Courbe interactive ---
    fig = px.line(
        df_volume,
        x="sales_agent",
        y="nb_ventes",
        markers=True,
        title="Volume de ventes par agent",
        labels={"sales_agent": "Agent commercial", "nb_ventes": "Nombre de ventes conclues"},
        line_shape="linear"
    )

    fig.update_traces(line=dict(color="teal", width=2), marker=dict(size=8, color="darkorange"))

    fig.update_layout(
        width=600, height=400,
        plot_bgcolor="#F9F9F9",
        paper_bgcolor="#F9F9F9",
        title_font=dict(size=18, color="#333333", family="Arial"),
        font=dict(size=12, family="Arial"),
        xaxis=dict(
            tickangle=45,
            showgrid=True,
            gridcolor="lightgrey",
            griddash="dot"
        ),
        yaxis=dict(
            title="Nombre de ventes conclues",
            showgrid=True,
            gridcolor="lightgrey",
            griddash="dot"
        )
    )

    # --- Affichage du graphique ---
    st.plotly_chart(fig, use_container_width=True)

    # --- Message résumé ---
    agent_max = df_volume.sort_values(by='nb_ventes', ascending=False).iloc[0]
    st.success(
        f"🏆 L’agent ayant conclu le plus de ventes est **{agent_max['sales_agent']}** "
        f"avec **{agent_max['nb_ventes']}** opportunités réussies."
    )