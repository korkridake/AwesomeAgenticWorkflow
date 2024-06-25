# filename: google_stock_analysis.py

import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

# Get the current date
current_date = datetime.now().strftime("%Y-%m-%d")

# Define the start date (beginning of the year)
start_date = f"{datetime.now().year}-01-01"

# Download Google stock data
ticker = "GOOGL"
data = yf.download(ticker, start=start_date, end=current_date)

# Check if data is available
if data.empty:
    print("No data found for the specified date range.")
else:
    # Perform bivariate analysis
    # Plotting Closing Price vs Volume
    plt.figure(figsize=(14, 7))
    sns.scatterplot(x=data['Volume'], y=data['Close'])
    plt.title('Bivariate Analysis of Google Stock (Closing Price vs Volume)')
    plt.xlabel('Volume')
    plt.ylabel('Closing Price')
    plt.grid(True)
    
    # Save the plot to a file
    plt.savefig('google_analysis.png')
    plt.show()

    # Print the first few rows of the data for reference
    print(data.head())