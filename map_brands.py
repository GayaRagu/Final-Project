
import plotly.express as px
from jupyter_dash import JupyterDash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import pandas as pd


# Load Data
df = pd.read_csv('mapdata.csv')
# Build App
app = JupyterDash(__name__)
app.layout = html.Div([
    html.H1("Perceptual Map of Brand Affinity"),
    dcc.Graph(id='graph'),
    html.Label([
        "colorscale",
        dcc.Dropdown(
            id='colorscale-dropdown', clearable=False,
            value='plasma', options=[
                {'label': c, 'value': c}
                for c in px.colors.named_colorscales()
            ])
    ]),
])
# Define callback to update graph
@app.callback(
    Output('graph', 'figure'),
    [Input("colorscale-dropdown", "value")]
)
def update_figure(colorscale):
    return px.scatter(
        df, x="x", y="y", color="cluster",
        color_continuous_scale=colorscale,
        render_mode="webgl", title="Perceptual Map",hover_data=['brand'],height=1000
    )
# Run app and display result inline in the notebook
app.run_server(mode='external')
