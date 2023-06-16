from keras.layers import Dense, LSTM
from keras.models import Sequential


def buildLSTMNetworkArch(data: any):
    model = Sequential()
    model.add(LSTM(128, return_sequences=True,
              input_shape=(data.shape[1], 1)))
    model.add(LSTM(64, return_sequences=False))
    model.add(Dense(25))
    model.add(Dense(1))
    model.summary()
    return model


def trainLSTNetwork(model: Sequential, inputTrainingData: any, targetTrainingData: any):
    model.compile(optimizer='adam', loss='mean_squared_error')
    model.fit(inputTrainingData, targetTrainingData, batch_size=1, epochs=30)
