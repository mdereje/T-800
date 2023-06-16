import numpy as np
from datetime import date, timedelta
from yahoo_finance_data_fetch import getDataForDay, getLastNDaysForSymbol
from utils.print import printAsBanner
from network import buildLSTMNetworkArch, trainLSTNetwork
from display import createAndDisplayCandleStick
from model import splitToTrainingAndTest

symbol = 'AAPL'
lookbackDays = 5000


# Retrieve and display
printAsBanner(
    f"Retreive data for {symbol} for the last {lookbackDays} days from yahoo")
data = getLastNDaysForSymbol(symbol, lookbackDays)

printAsBanner("Launch graph as a candel stick")
createAndDisplayCandleStick(data)

# Look at the correlation of all the columns with Close column
printAsBanner("Look at the coolrelation of all cols with close column")
correlation = data.corr()
print(correlation["Close"].sort_values(ascending=False))

# Traning LSTM for Stock Price Prediction
printAsBanner("Split the data into test and traning")
xtrain, xtest, ytrain, ytest = splitToTrainingAndTest(data=data, traningProperties=[
                                                      "Open", "High", "Low", "Volume"], targetProperty="Close")
print(f"==>> xtrain: {xtrain.size}")
print(f"==>> xtest: {xtest.size}")
print(f"==>> ytrain: {ytrain.size}")
print(f"==>> ytest: {ytest.size}")

# Neural network architecture for LSTM
printAsBanner("Build the neural network archietcture for LSTM")
model = buildLSTMNetworkArch(xtrain)

# # Train the neural network model
printAsBanner("Train the model for set architecture")
trainLSTNetwork(model, xtrain, ytrain)


# Fetch super test data
printAsBanner(
    "Test the model by feeding it set data data.[Open, High, Low, Volume]")
date_to_search = date.today() - timedelta(days=3)
date_to_search = date_to_search.strftime("%Y-%m-%d")
one_day_data = getDataForDay(symbol, date_to_search)
normal_array = [one_day_data.Open.values[0], one_day_data.High.values[0],
                one_day_data.Low.values[0], one_day_data.Volume.values[0]]
result_as_features = np.array([normal_array])

prediction = model.predict(result_as_features)
# Post search
post_date_to_search = date.today() - timedelta(days=2)
post_date_to_search = post_date_to_search.strftime("%Y-%m-%d")
post_one_day_data = getDataForDay(symbol, date_to_search)
print(f"test date: {date_to_search} => 'data' : {one_day_data.tail()}")
print(f'prediction -> {prediction}')
print(
    f"actual result for date: {post_date_to_search} => 'data' : {post_one_day_data.tail()}")
