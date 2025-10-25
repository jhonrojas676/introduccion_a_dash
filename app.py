import plotly.express as px
from dash import Dash, dcc, html

app = Dash(__name__)

print("=== CREANDO GRAFICO DE PIE ===")
# Gráfico de pie original
datos_tips = px.data.tips()
mi_figura_pie = px.pie(datos_tips, names="sex", values="tip", title="Distribucion de Propinas por Sexo")
print(" Gráfico de PIE creado")

print(" CREANDO GRAFICO DE BARRAS ")
# Gráfico de barras con gapminder
datos_gapminder = px.data.gapminder()
datos_2007 = datos_gapminder[datos_gapminder['year'] == 2007]
fig_barras_poblacion = px.bar(
    datos_2007.head(20),
    x="country", 
    y="pop",
    title="Poblacion por Pais (2007)",
    labels={"pop": "Poblacion", "country": "Pais"}
)
fig_barras_poblacion.update_layout(xaxis_tickangle=-45)

# layout final
app.layout = html.Div([
    html.H1("Aplicacion Dash - Dos Graficos"),
    
    html.Div([
        html.H2("Grafico de Pie - Datos Tips"),
        dcc.Graph(figure=mi_figura_pie)
    ]),
    
    html.Div([
        html.H2("Grafico de Barras - Datos Gapminder"),
        dcc.Graph(figure=fig_barras_poblacion)
    ])
])



if __name__ == '__main__':
    app.run(debug=True, use_reloader=False, port=8051)  # Puerto diferente, solucion propuesta por chat