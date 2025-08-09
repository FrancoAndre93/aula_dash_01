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

    dcc.Graph(id="grafico-colunas"),
    dcc.Graph(id="grafico-linha"),
    dcc.Graph(id="grafico-dispersao")
])

@app.callback(
    Output("grafico-colunas", "figure"),
    Output("grafico-linha", "figure"),
    Output("grafico-dispersao", "figure"),
    Input("dropdown-cidade", "value")
)
def atualizar_graficos(cidade_selecionada):
    df_filtrado = df[df["Cidade"] == cidade_selecionada]

    fig_colunas = px.bar(
        df_filtrado,
        x="Mês",
        y="Vendas",
        title=f"Vendas em {cidade_selecionada}",
        text="Vendas"
    )
    fig_colunas.update_traces(textposition='outside')

    fig_linha = px.line(
        df_filtrado,
        x="Mês",
        y="Vendas",
        title=f"Tendência de Vendas {cidade_selecionada}",
        markers=True
    )

    if "Quantidade" not in df_filtrado.columns:
        df_filtrado["Quantidade"] = df_filtrado["Vendas"] // 100  

    fig_disp = px.scatter(
        df_filtrado,
        x="Quantidade",
        y="Vendas",
        size="Vendas",
        color="Mês",
        title=f"Vendas x Quantidade {cidade_selecionada}",
        hover_name="Mês"
    )

    return fig_colunas, fig_linha, fig_disp

app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8050)))
