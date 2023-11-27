# Import packages
from dash import Dash, html, dash_table, dcc, callback, Output, Input
import pandas as pd
import plotly.express as px

# Incorporate data
df = pd.read_csv('https://raw.githubusercontent.com/IvanMA4HEB/dashboard/main/dara.csv')

# Initialize the app
app = Dash(__name__)


# App layout
app.layout = html.Div([
    html.Div(children='Выступления'),
    html.Hr(),
    dcc.RadioItems(options=['ветер день', 'Температура день'], value='ветер день', id='controls-and-radio-item'),
    dash_table.DataTable(data=df.to_dict('records'), page_size=10),
    dcc.Graph(figure={}, id='controls-and-graph'),
    dcc.Graph(figure=px.line(df, x='id города', y='давление день')),
    dcc.Graph(figure=px.pie(df, values='id города', names='облачность день')),
    dcc.Graph(figure=px.bar(df, x='ветер день', y='id города'))
])

# Add controls to build the interaction
@callback(
    Output(component_id='controls-and-graph', component_property='figure'),
    Input(component_id='controls-and-radio-item', component_property='value')
)
def update_graph(col_chosen):
    fig = px.histogram(df, x='id города', y=col_chosen, histfunc='avg')
    return fig

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
