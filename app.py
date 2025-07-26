import dash
from dash import dcc, html, Input, Output
import os
import plotly.express as px
import pandas as pd

df = pd.read_csv("vendas.csv")

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Dashboard Interativo de Vendas"),

    html.Label("Escolha a cidade:"),
    dcc.Dropdown(
        id="dropdown-cidade",
        options=[{"label": c, "value": c} for c in df["Cidade"].unique()],
        value="São Paulo"
    ),

    dcc.Graph(id="grafico-vendas")
])

@app.callback(
    Output("grafico-vendas", "figure"),
    Input("dropdown-cidade", "value")
)

def atualizar_grafico(cidade_selecionada):
    df_filtrado = df[df["Cidade"] == cidade_selecionada]
    fig = px.bar(
        df_filtrado,
        x="Mês",
        y="Vendas",
        title=f"Vendas em {cidade_selecionada}",
        text="Vendas"  
    )

    fig.update_traces(
        textposition='outside',  
        textfont_size=10
    )

    fig.update_layout(
        xaxis_title="Mês",
        yaxis_title="Vendas",
        title_font_size=20,
        xaxis_tickfont=dict(size=10),
        yaxis_tickfont=dict(size=10),
        margin=dict(l=40, r=20, t=60, b=40)
    )

    return fig


app.run(host="0.0.0.0",port=int(os.environ.get("PORT",8050)))