import dash
from dash import dcc, html  # Directly import from dash
import plotly.graph_objs as go
import pandas as pd
from dash.dependencies import Input, Output

# Load the categorized tasks data from CSV
df = pd.read_csv("categorized_data.csv")

# Calculate the total elapsed time per category (convert elapsed time to seconds)
df['Elapsed Time (Seconds)'] = df['Elapsed Time'].apply(
    lambda x: sum(int(i) * 60**(2-i) for i, x in enumerate(x.split(":"))) if isinstance(x, str) else 0)

# Group data by category and calculate the total time per category
category_totals = df.groupby('Category')['Elapsed Time (Seconds)'].sum().sort_values(ascending=False)

# Initialize Dash app
app = dash.Dash(__name__)

# Define the layout of the dashboard
app.layout = html.Div([
    html.H1("Task Time Dashboard", style={'textAlign': 'center'}),
    
    # Dropdown to select category for exploration
    html.Div([
        html.Label("Select a category:"),
        dcc.Dropdown(
            id='category-dropdown',
            options=[{'label': cat, 'value': cat} for cat in category_totals.index],
            value=category_totals.index[0],  # Default value
            style={'width': '50%'}
        )
    ], style={'padding': '10px', 'width': '50%', 'margin': '0 auto'}),

    # Graph to show total elapsed time per category
    dcc.Graph(id='category-time-graph'),

    # Graph to show individual tasks within selected category
    dcc.Graph(id='task-time-graph')
])


# Define callback to update the total category time graph
@app.callback(
    Output('category-time-graph', 'figure'),
    Input('category-dropdown', 'value')
)
def update_category_time_graph(selected_category):
    # Plot total elapsed time per category (Bar chart)
    fig = go.Figure([go.Bar(
        x=category_totals.index,
        y=category_totals.values,
        marker=dict(color='skyblue'),
    )])

    fig.update_layout(
        title="Total Elapsed Time per Category",
        xaxis_title="Category",
        yaxis_title="Total Elapsed Time (Seconds)",
        template="plotly_dark",
        plot_bgcolor='rgba(0, 0, 0, 0)',
    )
    return fig


# Define callback to update the tasks graph for selected category
@app.callback(
    Output('task-time-graph', 'figure'),
    Input('category-dropdown', 'value')
)
def update_task_time_graph(selected_category):
    # Filter data for selected category
    filtered_df = df[df['Category'] == selected_category]

    # Plot tasks and their elapsed time for the selected category
    fig = go.Figure([go.Bar(
        x=filtered_df['Task Name'],
        y=filtered_df['Elapsed Time (Seconds)'],
        marker=dict(color='lightgreen'),
    )])

    fig.update_layout(
        title=f"Tasks in Category: {selected_category}",
        xaxis_title="Task Name",
        yaxis_title="Elapsed Time (Seconds)",
        template="plotly_dark",
        plot_bgcolor='rgba(0, 0, 0, 0)',
        xaxis_tickangle=-45
    )
    return fig


# Run the Dash app
if __name__ == '__main__':
    app.run_server(debug=True)
