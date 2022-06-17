
from matplotlib.pyplot import figure
from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app=Dash(__name__)

df=pd.read_csv('webapp.csv',header=0,delimiter=',',encoding='unicode_escape')

# pip install dash

fig = px.bar(df, x='Fruit',y='Amount',color='City', barmode='group')
app.layout = html.Div(children =[

html.H1(children = 'Hello Data Analytic'),
dcc.Graph(id='my-graph', figure=fig)

])



if __name__ == '__main__':
    app.run_server(debug=True, port=8050)
