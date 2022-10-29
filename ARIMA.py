import stat
import statistics as stat
import pandas as pd
import numpy as np
import pandas_datareader as web
import datetime as dt
import pandas_datareader as web
import matplotlib.pyplot as plt

arr = list(web.DataReader("BTC-AUD", "yahoo", "2012-1-1", dt.datetime.now())['Close'].values)

window_size = 3
data = web.DataReader("BTC-AUD", "yahoo", "2012-1-1", dt.datetime.now())['Close']
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

for i in range(0, 500):
    newma = (moving_averages[len(moving_averages)-1]+meandifference)
    prediction = newma*3-arr[len(arr)-1]-arr[len(arr)-2]
    predictions.append(prediction)
    moving_averages.append(newma)

predictiondates = []

for i in range(0, 500):
    date = dt.datetime.now()+dt.timedelta(days=i)
    predictiondates.append(date)

plt.plot(data, label="actual stocks")
plt.plot(predictiondates, predictions, label="Predictions")
plt.legend()
plt.show()