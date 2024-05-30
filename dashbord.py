import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd

# Chargez vos données pour le tableau de bord
df = pd.read_csv('chemin_vers_votre_fichier.csv')

# Initialisez l'application Dash
app = dash.Dash(__name__)

# Définissez la mise en page du tableau de bord
app.layout = html.Div([
    html.H1("Tableau de bord des startups en Île-de-France"),
    
    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': df['Nom'], 'y': df['Financement'], 'type': 'bar', 'name': 'Financement'},
            ],
            'layout': {
                'title': 'Financement des startups en Île-de-France'
            }
        }
    ),
])

# Exécutez l'application Dash
if __name__ == '__main__':
    app.run_server(debug=True)
