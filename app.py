import plotly.express as px
from dash import Dash, dcc, html  


app= Dash() # inicia una aplicacion

datos = px.data.tips() # guarda los datos de plotly express
#guarda el grafico en una variable
mi_figura= px.pie(datos,names="sex", values="tip")

app.layout = html.Div([
    dcc.Graph(figure=mi_figura)
])

app.run(debug=True, use_reloader=False)