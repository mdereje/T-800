from pandas import DataFrame
from sklearn.model_selection import train_test_split


def splitToTrainingAndTest(data: DataFrame, traningProperties: list[str], targetProperty: str):
    x = data[traningProperties]
    y = data[targetProperty]
    x = x.to_numpy()
    y = y.to_numpy()
    y = y.reshape(-1, 1)

    return train_test_split(
        x, y, test_size=0.2, random_state=42)
