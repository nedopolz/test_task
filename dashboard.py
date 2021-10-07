import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px

import pandas as pd

app = dash.Dash(__name__)

lines = pd.read_csv(r'data.csv',
                    sep=';')
poses = lines['INTERNAL_ORG_ORIGINAL_RK'].unique()
poses = list(poses)
poses.sort()
poses = [str(i) for i in poses]
df = pd.read_csv(
    r'data_out.csv', sep=',',
    skiprows=0, index_col='Date/Pos')


app.layout = html.Div([
    html.Div([
        html.Div([
            dcc.Dropdown(
                id='pos_id',
                options=[{'label': i, 'value': i} for i in poses],
                value=''
            ),
            dcc.RadioItems(
                id='type',
                options=[{'label': i, 'value': i} for i in ['absolute', 'percentage']],
                value='Linear',
                labelStyle={'display': 'inline-block'}
            )
        ], style={'width': '48%', 'display': 'inline-block'}),
    ]),
    dcc.Graph(id='indicator-graphic'),
])


@app.callback(
    Output('indicator-graphic', 'figure'),
    Input('pos_id', 'value'),
    Input('type', 'value')
)
def update_graph(pos_id, type):
    if not pos_id:
        pos_id = poses[0]
    post = ''

    if type == 'percentage':
        post = '%'

    new_df = df[f'{pos_id}{post}']
    fig = px.line(new_df, title="A pos income chart")
    return fig


if __name__ == '__main__':
    app.run_server(debug=True)
