from datetime import date, timedelta
import yfinance as yf
from time_util import addDayToStringDateAndReturnFormatted


def getDataForDay(symbol: str, date_to_fetch: str):
    """ Fetch stock features [Open, High, Low, Adj Close, Volume] for specific date 
    Args:
        date_to_fetch (str): Download for date (YYYY-MM-DD).
            Default is 1900-01-01
            E.g. for start="2020-01-01", the first data point will be on "2020-01-01"
    """
    end_date = addDayToStringDateAndReturnFormatted(date_to_fetch, 1)

    data = yf.download(symbol, start=date_to_fetch,
                       end=end_date, progress=False)
    data["Date"] = data.index

    data = data[["Date", "Open", "High",
                 "Low", "Close", "Adj Close", "Volume"]]
    data.reset_index(drop=True, inplace=True)

    return data


def getLastNDaysForSymbol(symbol: str, lookBackDays: str):
    # Get the data from yahoo finance and print the last 5
    today = date.today()

    d1 = today.strftime("%Y-%m-%d")
    end_date = d1

    d2 = date.today() - timedelta(days=lookBackDays)
    d2 = d2.strftime("%Y-%m-%d")
    start_date = d2

    data = yf.download(symbol, start=start_date, end=end_date, progress=False)
    data["Date"] = data.index

    data = data[["Date", "Open", "High",
                 "Low", "Close", "Adj Close", "Volume"]]
    data.reset_index(drop=True, inplace=True)
    # data.tail()  # returns the last 5
    print(f"==>> data.tail(): {data.tail()}")
    return data
