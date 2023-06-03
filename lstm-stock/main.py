import numpy as np
from keras.layers import Dense, LSTM
from keras.models import Sequential
from sklearn.model_selection import train_test_split
import plotly.graph_objects as go
import pandas as pd
import yfinance as yf
import datetime
from datetime import date, timedelta


print(
    '''
=======================================
|									 |
|									 |
 Retreive and display data from yahoo
|									 |
|									 |
=======================================
'''
)

# Get the data from yahoo finance and print the last 5
today = date.today()

d1 = today.strftime("%Y-%m-%d")
end_date = d1

d2 = date.today() - timedelta(days=5000)
d2 = d2.strftime("%Y-%m-%d")
start_date = d2

data = yf.download('AAPL', start=start_date, end=end_date, progress=False)
data["Date"] = data.index

data = data[["Date", "Open", "High", "Low", "Close", "Adj Close", "Volume"]]
data.reset_index(drop=True, inplace=True)
# data.tail()  # returns the last 5
print(f"==>> data.tail(): {data.tail()}")


print(
    '''
=======================================
|									 |
|									 |
 Launch graph as a candel stick
|									 |
|									 |
=======================================
'''
)

# Display the graph as a candle stick
figure = go.Figure(data=[go.Candlestick(x=data["Date"], open=data["Open"],
                   high=data["High"], low=data["Low"], close=data["Close"])])

figure.update_layout(title="Apple Stock Price Analysis",
                     xaxis_rangeslider_visible=False)

figure.show()  # No need to show yet, this could be useful for other means.


print(
    '''
=======================================
|									 |
|									 |
 look at the correlation of all cols |
| with the close column.			 |
|									 |
=======================================
'''
)
# Look at the correlation of all the columns with Close column
correlation = data.corr()
print(correlation["Close"].sort_values(ascending=False))


print(
    '''
=======================================
|									 |
|									 |
 Split the data into test and traning
|									 |
|									 |
=======================================
'''
)
# Traning LSTM for Stock Price Prediction
x = data[["Open", "High", "Low", "Volume"]]
y = data["Close"]

x = x.to_numpy()
y = y.to_numpy()
y = y.reshape(-1, 1)

xtrain, xtest, ytrain, ytest = train_test_split(
    x, y, test_size=0.2, random_state=42)  # not sure what the random_state is here.
print(f"==>> xtrain: {xtrain.size}")
print(f"==>> xtest: {xtest.size}")
print(f"==>> ytrain: {ytrain.size}")
print(f"==>> ytest: {ytest.size}")

print(
    '''
=======================================
|									 |
|									 |
 Build the neural network archietcture
| for LSTM  						 |
|									 |
=======================================
'''
)
# Neural network architecture for LSTM
model = Sequential()
model.add(LSTM(128, return_sequences=True, input_shape=(xtrain.shape[1], 1)))
model.add(LSTM(64, return_sequences=False))
model.add(Dense(25))
model.add(Dense(1))
model.summary()

print(
    '''
=======================================
|									 |
|									 |
 Train the model for set architecture|
|               					 |
|									 |
=======================================
'''
)

# # Train the neural network model
model.compile(optimizer='adam', loss='mean_squared_error')
model.fit(xtrain, ytrain, batch_size=1, epochs=30)


print(
    '''
=======================================
 Test the model by feeding it        
 set data data.   
[Open, High, Low, Adj Close, Volume]
[177.089996, 180.419998, 177.070007, 74919600]
=======================================
'''
)
# Test the model
# features = [Open, High, Low, Adj Close, Volume]
features = np.array([[177.089996, 180.419998, 177.070007, 74919600]])
print(f'prediction -> {model.predict(features)}')
