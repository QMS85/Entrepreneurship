import streamlit as st
import pandas as pd
import plotly.express as px

def display_progress_bar(percentage, label=""):
    """
    Displays a custom progress bar in Streamlit
    
    Parameters:
    percentage (float): Value between 0 and 1
    label (str): Label for the progress bar
    """
    if percentage < 0:
        percentage = 0
    if percentage > 1:
        percentage = 1
        
    # Display the progress bar
    st.progress(percentage)
    if label:
        st.caption(label)

def create_comparison_chart(data, x_column, y_column, size_column=None, 
                           color_column=None, title="", hover_name=None):
    """
    Creates a scatter plot for comparison using Plotly
    
    Parameters:
    data (pandas.DataFrame): Data to plot
    x_column (str): Column name for x-axis
    y_column (str): Column name for y-axis
    size_column (str, optional): Column name for point size
    color_column (str, optional): Column name for point color
    title (str): Chart title
    hover_name (str, optional): Column to use for hover labels
    
    Returns:
    plotly.graph_objects.Figure: The created figure
    """
    if size_column:
        if color_column:
            fig = px.scatter(
                data, x=x_column, y=y_column, 
                size=size_column, color=color_column,
                hover_name=hover_name if hover_name else x_column,
                title=title
            )
        else:
            fig = px.scatter(
                data, x=x_column, y=y_column, 
                size=size_column,
                hover_name=hover_name if hover_name else x_column,
                title=title
            )
    else:
        if color_column:
            fig = px.scatter(
                data, x=x_column, y=y_column, 
                color=color_column,
                hover_name=hover_name if hover_name else x_column,
                title=title
            )
        else:
            fig = px.scatter(
                data, x=x_column, y=y_column,
                hover_name=hover_name if hover_name else x_column,
                title=title
            )
    
    return fig

def display_resource_card(title, description, url=None, icon="📚"):
    """
    Displays a formatted resource card
    
    Parameters:
    title (str): Resource title
    description (str): Resource description
    url (str, optional): URL to link to
    icon (str): Emoji icon to display
    """
    st.markdown(f"### {icon} {title}")
    st.markdown(description)
    if url:
        st.markdown(f"[Learn more]({url})")
    st.markdown("---")
