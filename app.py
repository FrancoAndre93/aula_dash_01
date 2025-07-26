import dash
from dash import html, dcc
import plotly.express as px
import pandas as pd

df = pd.DataFrame({
    "Mês":['Jan', 'Fev', 'Mar', 'Abr', 'Mai'],
    "Vendas": [100,120,50, 200, 180]
})

fig = px.line(df, x='Mês', y='Vendas')
app = dash.Dash(__name__)
app.layout = html.Div([
    html.H1("Dashboard de vendas", 
            style={'textAlign':'center'}),
    dcc.Graph(figure=fig)
])

if __name__ == "__main__":
  app.run()