import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file
    df = pd.read_csv('sample_data/epa-sea-level.csv')
  
    # 1st graph
    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']
    n = np.size(x)
    
    x_mean = np.mean(x)
    y_mean = np.mean(y)
    
    Sxy = np.sum(x*y)- n*x_mean*y_mean
    Sxx = np.sum(x*x)-n*x_mean*x_mean
    b1 = Sxy/Sxx
    b0 = y_mean-b1*x_mean
    print('slope b1 is', b1)
    print('intercept b0 is', b0)
    
    plt.scatter(x, y,
                linewidths = 1,
                s = 10,)
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    
    res = linregress(x, y)
    x_pred = pd.Series([i for i in range(1880,2051)])
    y_pred = res.intercept + res.slope*x_pred
    plt.plot(x_pred, y_pred, 'r')
    
    plt.title('Rise in sea level')

    # 2nd graph
    df_adj = df.loc[df['Year'] >= 2000]
    x_adj = df_adj['Year'] 
    y_adj = df_adj['CSIRO Adjusted Sea Level']
    
    x_mean_2 = np.mean(x_adj)
    y_mean_2 = np.mean(y_adj)
    
    Sxy_2 = np.sum(x_adj*y_adj)- n*x_mean_2*y_mean_2
    Sxx_2 = np.sum(x*x)-n*x_mean*x_mean
    a1 = Sxy_2/Sxx_2
    a0 = y_mean_2-a1*x_mean_2
    print('slope a1 is', a1)
    print('intercept a0 is', a0)
    
    plt.scatter(x_adj, y_adj,
                linewidths = 1,
                s = 10,)
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    
    res_2 = linregress(x_adj, y_adj)
    x_pred_2 = pd.Series([i for i in range(2000,2051)])
    y_pred_2 = res_2.intercept + res_2.slope*x_pred_2
    plt.plot(x_pred_2, y_pred_2, 'r')
    
    plt.title('Rise in sea level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()