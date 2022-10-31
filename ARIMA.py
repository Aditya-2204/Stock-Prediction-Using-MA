import statistics as stat
import pandas as pd
import numpy as np
import pandas_datareader as web
import datetime as dt
import pandas_datareader as web
import matplotlib.pyplot as plt

stock = "DOGE-AUD"
daysofprediction = 500

arr = list(web.DataReader(stock, "yahoo", "2012-1-1", dt.datetime.now())['Close'].values)

window_size = 3
data = web.DataReader(stock, "yahoo", "2012-1-1", dt.datetime.now())['Close']
numbers_series = pd.Series(arr)
windows = numbers_series.rolling(window_size)

moving_averages = windows.mean()
moving_averages = list(moving_averages[2:].values)

differences = []

for i in range(0, len(moving_averages)-1):
    diff = moving_averages[i+1]-moving_averages[i]
    differences.append(diff)

meandifference = stat.mean(differences)
predictions = []

for i in range(0, daysofprediction):
    newma = (moving_averages[len(moving_averages)-1]+meandifference)
    prediction = newma*3-arr[len(arr)-1]-arr[len(arr)-2]
    predictions.append(prediction)
    moving_averages.append(newma)

predictiondates = []

for i in range(0, daysofprediction):
    date = dt.datetime.now()+dt.timedelta(days=i)
    predictiondates.append(date)

rate = predictions[len(predictions)-1]-predictions[0]/predictiondates[len(predictiondates)-1]-predictiondates[0]

if predictions[len(predictions)-1]>predictions[0]:
    plt.plot(data, label="actual stocks")
    plt.plot(predictiondates, predictions, label="Predictions", color="green")
    plt.xlabel("Time")
    plt.ylabel("Price")
    plt.title(f"{stock} Price Prediction")
    plt.legend()
    plt.show()
if predictions[len(predictions)-1]<predictions[0]:
    plt.plot(data, label="actual stocks")
    plt.plot(predictiondates, predictions, label="Predictions", color="red")
    plt.xlabel("Time")
    plt.ylabel("Price")
    plt.title(f"{stock} Price Prediction")
    plt.legend()
    plt.show()
if predictions[len(predictions)-1]==predictions[0]:
    plt.plot(data, label="actual stocks")
    plt.plot(predictiondates, predictions, label="Predictions", color="black")
    plt.xlabel("Time")
    plt.ylabel("Price")
    plt.title(f"{stock} Price Prediction")
    plt.legend()
    plt.show()
