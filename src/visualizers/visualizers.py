import sys
import os
from pandas import DataFrame
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Dynamically add the src folder to the Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
src_dir = os.path.dirname(current_dir)

if src_dir not in sys.path:
    sys.path.append(src_dir)

def plot_energy_revenue(df, time_interval):
    # Resample the data based on the chosen time interval
    if time_interval == 'Day':
        resampled_data = df.resample('D', on='SETTLEMENTDATE').sum()
    elif time_interval == 'Month':
        resampled_data = df.resample('M', on='SETTLEMENTDATE').sum()
    elif time_interval == 'Hour':
        resampled_data = df.resample('H', on='SETTLEMENTDATE').sum()
    else:
        raise ValueError("Invalid time interval. Choose 'Day', 'Month', or 'Hour'.")
    
    # Create an interactive bar graph using Plotly
    fig = px.bar(resampled_data, x=resampled_data.index, y='REVENUE',
                 title=f'Energy Revenue Aggregated by {time_interval} for {df["Station Name"].iloc[0]}',
                 labels={'x': 'SETTLEMENTDATE', 'REVENUE': 'REVENUE'},
                 template='plotly')

    # Update hover template to only show revenue
    fig.update_traces(hovertemplate='Energy Revenue: %{y:.2f}<extra></extra>')

    # Update layout for better visualization
    fig.update_layout(xaxis_title="Date",
                      yaxis_title="Revenue",
                      xaxis_rangeslider_visible=True)
    
    fig.show()


def plot_regulation_revenue(df, time_interval):
    # Resample the data based on the chosen time interval
    if time_interval == 'Day':
        resampled_data = df.resample('D', on='SETTLEMENTDATE').sum()
    elif time_interval == 'Month':
        resampled_data = df.resample('M', on='SETTLEMENTDATE').sum()
    elif time_interval == 'Hour':
        resampled_data = df.resample('H', on='SETTLEMENTDATE').sum()
    else:
        raise ValueError("Invalid time interval. Choose 'Day', 'Month', or 'Hour'.")

    # Compute the total revenue for each aggregated period
    resampled_data['TotalRevenue'] = resampled_data[['RAISEREGREVENUE', 'LOWERREGREVENUE']].sum(axis=1)

    # Create an interactive bar graph using Plotly
    fig = px.bar(resampled_data, x=resampled_data.index,
                 y=['RAISEREGREVENUE', 'LOWERREGREVENUE'],
                 title=f'Regulation Revenue Aggregated by {time_interval} for {df["Station Name"].iloc[0]}',
                 labels={'x': 'SETTLEMENTDATE', 'value': 'REVENUE', 'variable': 'Type of Revenue'},
                 template='plotly', color_discrete_map={'RAISEREGREVENUE': 'green', 'LOWERREGREVENUE': 'orange'})
    
    # Assigning custom hover data and updating hover template to reflect correct labels
    hover_labels = ['Raise Regulation Revenue', 'Lower Regulation Revenue']
    for i, trace in enumerate(fig.data):
        trace.customdata = resampled_data['TotalRevenue']
        trace.hovertemplate = f'{hover_labels[i]}: %{{y:.1f}}<br>Total: %{{customdata:.1f}}<extra></extra>'

    # Update layout for better visualization
    fig.update_layout(xaxis_title="Date",
                      yaxis_title="Revenue",
                      xaxis_rangeslider_visible=True)

    fig.show()


def plot_contingency_revenue(df, time_interval):
    # Resample the data based on the chosen time interval
    if time_interval == 'Day':
        resampled_data = df.resample('D', on='SETTLEMENTDATE').sum()
    elif time_interval == 'Month':
        resampled_data = df.resample('M', on='SETTLEMENTDATE').sum()
    elif time_interval == 'Hour':
        resampled_data = df.resample('H', on='SETTLEMENTDATE').sum()
    else:
        raise ValueError("Invalid time interval. Choose 'Day', 'Month', or 'Hour'.")

    # Define the columns for RAISE and LOWER series
    raise_columns = ['RAISE1SECREVENUE', 'RAISE6SECREVENUE', 'RAISE60SECREVENUE', 'RAISE5MINREVENUE']
    lower_columns = ['LOWER1SECREVENUE', 'LOWER6SECREVENUE', 'LOWER60SECREVENUE', 'LOWER5MINREVENUE']

    # Define the color palettes for RAISE and LOWER series with distinct colors
    raise_colors = ['#9c27b0', '#1f77b4', '#6baed6', '#3182bd']  # Different shades of purple
    lower_colors = ['#ffeb3b', '#ffc107', '#ff9800', '#ff5722']  # Different shades of yellow

    # Compute the total revenue for each bar
    resampled_data['Total'] = resampled_data[raise_columns + lower_columns].sum(axis=1)

    # Create the figure with subplots
    fig = go.Figure()

    # Labels for hover text
    raise_labels = ["Raise 1 Second Revenue", "Raise 6 Second Revenue", "Raise 60 Second Revenue", "Raise 5 Minute Revenue"]
    lower_labels = ["Lower 1 Second Revenue", "Lower 6 Second Revenue", "Lower 60 Second Revenue", "Lower 5 Minute Revenue"]

    # Add RAISE series, stacked
    for i, col in enumerate(raise_columns):
        fig.add_trace(go.Bar(x=resampled_data.index, y=resampled_data[col],
                             name=raise_labels[i], marker_color=raise_colors[i],
                             hovertemplate=f"%{{data.name}}: %{{y:.1f}}<br>Total: %{{customdata:.1f}}<extra></extra>"))

    # Add LOWER series, stacked
    for i, col in enumerate(lower_columns):
        fig.add_trace(go.Bar(x=resampled_data.index, y=resampled_data[col],
                             name=lower_labels[i], marker_color=lower_colors[i], offsetgroup=1,
                             hovertemplate=f"%{{data.name}}: %{{y:.1f}}<br>Total: %{{customdata:.1f}}<extra></extra>"))

    # Update layout to stack bars
    fig.update_layout(
        barmode='stack',
        title=f'Contingency Revenue Aggregated by {time_interval} for {df["Station Name"].iloc[0]}',
        xaxis_title="Date",
        yaxis_title="Revenue",
        xaxis_rangeslider_visible=True
    )

    # Update extra hover info with the total
    fig.update_traces(customdata=resampled_data['Total'].values)

    fig.show()