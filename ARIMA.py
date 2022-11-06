import statistics as stat
import pandas as pd
import numpy as np
import pandas_datareader as web
import datetime as dt
import pandas_datareader as web
import matplotlib.pyplot as plt
import streamlit as st

stock = "ETH-AUD"
daysofprediction = 20

arr = list(web.DataReader(stock, "yahoo", "2012-1-1", dt.datetime.now())['Close'].values)

window_size = 20
data = web.DataReader(stock, "yahoo", "2012-1-1", dt.datetime.now())['Close']
numbers_series = pd.Series(arr)
windows = numbers_series.rolling(window_size)

moving_averages = windows.mean()
moving_averages = list(moving_averages[19:].values)

differences = []

for i in range(0, len(moving_averages)-1):
    diff = moving_averages[i+1]-moving_averages[i]
    differences.append(diff)

meandifference = stat.mean(differences)
predictions = []

for i in range(0, window_size+1):
    newma = moving_averages[len(moving_averages)-1]
    newma = newma+meandifference
    prediction = newma*20-arr[len(arr)-1]-arr[len(arr)-2]-arr[len(arr)-3]-arr[len(arr)-4]-arr[len(arr)-5]-arr[len(arr)-6]-arr[len(arr)-7]-arr[len(arr)-8]-arr[len(arr)-9]-arr[len(arr)-10]-arr[len(arr)-11]-arr[len(arr)-12]-arr[len(arr)-13]-arr[len(arr)-14]-arr[len(arr)-15]-arr[len(arr)-16]-arr[len(arr)-17]-arr[len(arr)-18]-arr[len(arr)-19]
    predictions.append(prediction)
    moving_averages.append(newma)
    arr.append(prediction)
    print(prediction)

predictiondates = []
arr = arr[:len(arr)-21]

for i in range(0, window_size+1):
    date = dt.datetime.now()+dt.timedelta(days=i)
    predictiondates.append(date)


plt.plot(predictiondates, predictions, label="Predictions", color="red")
plt.plot(data.index, arr, label=f"Historical {stock} data")
plt.xlabel("Time")
plt.ylabel("Price")
plt.title(f"{stock} Price Prediction")
plt.legend()
plt.show()
