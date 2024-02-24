import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv',sep=',',header=0)

    # Create scatter plot - Use matplotlib to create a scatter plot using the Year column as the x-axis and the CSIRO Adjusted Sea Level column as the y-axis.
    fig, ax = plt.subplots(figsize=(15, 10))
    df.plot(kind='scatter', ax = ax,legend=True, fontsize=12,x='Year',y='CSIRO Adjusted Sea Level')
    ax.set_xlabel('Year', fontsize=15)
    ax.set_ylabel('CSIRO Adjusted Sea Level', fontsize=15)
    ax.set_title('Volume and percent change')


    # Create first line of best fit
    x_values = range(df['Year'].min(), 2051)
    slope, intercept, _, _, _ = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    plt.plot(x_values,slope*x_values+intercept, color = 'red')


    # Create second line of best fit
    x_values2 = range(2000, 2051)
    mask = df['Year'] >= 2000
    df2 = df[mask]
    df2.reset_index(drop=True, inplace=True)
    slope2, intercept2, _, _, _ = linregress(df2['Year'], df2['CSIRO Adjusted Sea Level'])
    plt.plot(x_values2,slope2*x_values2+intercept2, color = 'green')


    # Add labels and title
    plt.axvline(x=2013, linestyle='--', color='gray')
    ax.set_xlabel("Year", fontsize=12)
    ax.set_ylabel("Sea Level (inches)", fontsize=12)
    ax.set_title("Rise in Sea Level", fontsize=16)

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()

