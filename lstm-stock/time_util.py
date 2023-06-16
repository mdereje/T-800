from datetime import timedelta, datetime


def addDayToStringDateAndReturnFormatted(date: str, days: int):
    """ Fetch stock features [Open, High, Low, Adj Close, Volume] for specific date 
    Args:
        date (str): Date to add or subtract as string (YYYY-MM-DD).
            Default is 1900-01-01
            E.g. for start="2020-01-01", the first data point will be on "2020-01-01"
        days (int): Number of days to add or subtract
    """
    start_date = datetime.strptime(date, '%Y-%m-%d').date()
    end_date = start_date + timedelta(days=days)
    start_date = start_date.strftime("%Y-%m-%d")
    return end_date.strftime("%Y-%m-%d")
