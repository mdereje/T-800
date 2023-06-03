# lstm-stock

This is a project based on [Stock Price Prediction with LSTM](https://thecleverprogrammer.com/2022/01/03/stock-price-prediction-with-lstm/) created in order to learn and understand ML models.

## AI description

LSTM stands for Long Short-Term Memory. LSTMs are a type of recurrent neural network (RNN) that are capable of learning long-term dependencies. LSTMs are used in the fields of artificial intelligence and deep learning.
LSTMs are used to learn, process, and classify sequential data. Common LSTM applications include sentiment analysis, language modeling, speech recognition, and video analysis.
LSTMs have feedback connections, unlike standard feedforward neural networks. LSTMs have more gates and more parameters than GRUs, which gives them more flexibility and expressiveness, but also more computational cost and risk of overfitting.

## TO RUN

- `pip install -r requirements.txt`
- `python3 main.py`

## When addding new packages

- `cd <project>`
- `pip install <packagename>`
- `pip freeze > requiremnts.txt`

## Next steps

- See if this can be hosted somewhere so as you feed it new data it can respond with a prediction.
- It uses new data to also correct itself on the next day.
- See how to add other variables (such as twitter, news, reddit sentiment)
- Could be an API call
