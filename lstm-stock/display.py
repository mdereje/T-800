import plotly.graph_objects as go


def createAndDisplayCandleStick(data: any):
    figure = go.Figure(data=[go.Candlestick(x=data["Date"], open=data["Open"],
                                            high=data["High"], low=data["Low"], close=data["Close"])])

    figure.update_layout(title="Apple Stock Price Analysis",
                         xaxis_rangeslider_visible=False)

    figure.show()  # No need to show yet, this could be useful for other means.
