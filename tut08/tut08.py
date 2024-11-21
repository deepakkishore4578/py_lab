pip install mplfinance

import pandas as pd
import matplotlib.pyplot as plt
import mplfinance as mpf
import numpy as np

# task-1
data = pd.read_csv('infy_stock.csv')
print(data.head(10))
print(data.info())

# Display rows with missing values
missing_data = data[data.isnull().any(axis=1)]
# print(missing_data)
data_cleaned = data.dropna()
print(data_cleaned.info())

# task-2
closing_price=data_cleaned['Close']
time=data_cleaned['Date']

# Plot closing price over time
plt.figure(figsize=(10,6))
plt.plot(time, closing_price, label='Closing Price', color='b')

# Add labels and title
plt.xlabel('Date')
plt.ylabel('Closing Price')
plt.title('Closing Price Over Time')
# plt.xticks(rotation=45)  # Rotate the x-axis labels for better readability
# plt.legend()

# Display the plot
plt.tight_layout()
plt.show()

# task-2
# Select only the columns required for the candlestick chart: Open, High, Low, Close, Volume
ohlc_data = data_cleaned[['Open', 'High', 'Low', 'Close', 'Volume']]

# Plot the candlestick chart
mpf.plot(ohlc_data, type='candle', volume=True, style='charles', title='Candlestick Chart', ylabel='Price')

# task-3
# Extract 'Close' and 'Open' columns as lists
close_list = data_cleaned['Close'].tolist()
open_list = data_cleaned['Open'].tolist()

daily_returns = []
for i in range(len(close_list)):
  x=((close_list[i]-open_list[i])/open_list[i])*100
  daily_returns.append(x)
print(daily_returns[:10])
average_daily_return=np.mean(daily_returns)
median_daily_return=np.median(daily_returns)
print(average_daily_return)
print(median_daily_return)

# Calculate the standard deviation of the 'Close' prices
std_dev_close = data_cleaned['Close'].std()
print(f"Standard Deviation of Closing Prices: {std_dev_close:.2f}")

# task -4
# Convert 'Date' to datetime format for plotting purposes
data_cleaned['Date'] = pd.to_datetime(data_cleaned['Date'])

# Calculate the 50-day and 200-day moving averages
data_cleaned['50_MA'] = data_cleaned['Close'].rolling(window=50).mean()
data_cleaned['200_MA'] = data_cleaned['Close'].rolling(window=200).mean()

# Plot closing price along with moving averages
plt.figure(figsize=(10,6))
plt.plot(data_cleaned['Date'], data_cleaned['Close'], label='Close Price', color='blue')
plt.plot(data_cleaned['Date'], data_cleaned['50_MA'], label='50-Day MA', color='green')
plt.plot(data_cleaned['Date'], data_cleaned['200_MA'], label='200-Day MA', color='red')

plt.xlabel('Date')
plt.ylabel('Price')
plt.title('INFY Stock Closing Price with 50-day and 200-day Moving Averages')
plt.legend()
plt.tight_layout()
plt.show()

# task-5
# Calculate 30-day rolling standard deviation (volatility)
data_cleaned['30_Rolling_Std'] = data_cleaned['Close'].rolling(window=30).std()

# Plot the 30-day rolling standard deviation
plt.figure(figsize=(10,6))
plt.plot(data_cleaned['Date'], data_cleaned['30_Rolling_Std'], label='30-Day Rolling Std', color='purple')

plt.xlabel('Date')
plt.ylabel('Volatility (30-day rolling std)')
plt.title('INFY Stock Volatility (30-day Rolling Standard Deviation)')
plt.legend()
# plt.tight_layout()
plt.show()

# task-6
# Identify bullish and bearish trends
data_cleaned['Trend'] = np.where(data_cleaned['50_MA'] > data_cleaned['200_MA'], 'Bullish', 'Bearish')

# Plot the closing prices along with bullish/bearish markers
plt.figure(figsize=(10,6))
plt.plot(data_cleaned['Date'], data_cleaned['Close'], label='Close Price', color='blue')

# Mark bullish and bearish trends
bullish_trend = data_cleaned[data_cleaned['Trend'] == 'Bullish']
bearish_trend = data_cleaned[data_cleaned['Trend'] == 'Bearish']

plt.scatter(bullish_trend['Date'], bullish_trend['Close'], color='green', label='Bullish', marker='^', alpha=1)
plt.scatter(bearish_trend['Date'], bearish_trend['Close'], color='red', label='Bearish', marker='v', alpha=1)

plt.xlabel('Date')
plt.ylabel('Price')
plt.title('INFY Stock Price with Bullish and Bearish Trends')
plt.legend()
plt.tight_layout()
plt.show()

