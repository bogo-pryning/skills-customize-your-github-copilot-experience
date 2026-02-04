"""
Python Data Visualization Starter Code

This starter code provides a foundation for creating data visualizations
using matplotlib and plotly. Complete the tasks to build professional charts.
"""

import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np


class DataVisualizer:
    """A class to handle data visualization tasks with matplotlib and plotly."""
    
    def __init__(self):
        """Initialize the DataVisualizer with sample data."""
        self.data = None
        self.fig = None
    
    def load_sample_data(self):
        """
        Load sample data for visualization.
        
        Returns:
            pd.DataFrame: Sample dataset with months and values
        """
        # Sample data: monthly sales
        months = ['January', 'February', 'March', 'April', 'May', 'June',
                  'July', 'August', 'September', 'October', 'November', 'December']
        sales = [45000, 52000, 48000, 61000, 55000, 67000,
                 72000, 68000, 71000, 78000, 82000, 89000]
        
        self.data = pd.DataFrame({
            'Month': months,
            'Sales': sales,
            'Quarter': ['Q1', 'Q1', 'Q1', 'Q2', 'Q2', 'Q2',
                       'Q3', 'Q3', 'Q3', 'Q4', 'Q4', 'Q4']
        })
        
        return self.data
    
    def create_line_chart(self):
        """
        Create a line chart using matplotlib showing sales trends.
        
        TODO: Add title, labels, and styling
        """
        if self.data is None:
            self.load_sample_data()
        
        plt.figure(figsize=(10, 6))
        # TODO: Create your line chart here
        # plt.plot(self.data['Month'], self.data['Sales'])
        # Add title, labels, and formatting
        
        plt.tight_layout()
        return plt
    
    def create_bar_chart(self):
        """
        Create an interactive bar chart using plotly showing quarterly sales.
        
        TODO: Group data by quarter and create bar chart
        """
        if self.data is None:
            self.load_sample_data()
        
        # TODO: Create your bar chart here
        # Group data by quarter and visualize
        quarterly_sales = self.data.groupby('Quarter')['Sales'].sum()
        
        # Uncomment and complete this:
        # fig = go.Figure(data=[go.Bar(x=..., y=...)])
        # fig.update_layout(title=..., xaxis_title=..., yaxis_title=...)
        
        return None
    
    def create_scatter_plot(self):
        """
        Create an interactive scatter plot using plotly.
        
        TODO: Create scatter plot with custom styling
        """
        # TODO: Create your scatter plot here
        # You can use sample data or load your own
        
        return None
    
    def create_pie_chart(self):
        """
        Create a pie chart showing the distribution of sales by quarter.
        
        TODO: Calculate quarterly totals and create pie chart
        """
        if self.data is None:
            self.load_sample_data()
        
        # TODO: Create your pie chart here
        quarterly_totals = self.data.groupby('Quarter')['Sales'].sum()
        
        return None
    
    def save_chart(self, filename):
        """
        Save the current matplotlib figure to a file.
        
        Args:
            filename (str): Name of the file to save (e.g., 'chart.png')
        """
        # TODO: Implement chart saving
        pass


def init():
    """
    Initialize and run the data visualization examples.
    
    This is the main entry point for the program.
    """
    visualizer = DataVisualizer()
    visualizer.load_sample_data()
    
    print("Data Visualization Starter Code")
    print("=" * 40)
    print("\nSample Data:")
    print(visualizer.data)
    
    # TODO: Uncomment and complete the visualization tasks
    # visualizer.create_line_chart()
    # plt.show()
    
    # visualizer.create_bar_chart()
    # visualizer.fig.show()


if __name__ == "__main__":
    init()
