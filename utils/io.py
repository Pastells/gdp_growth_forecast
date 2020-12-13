"""Read and write into dataset"""

import sqlite3
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from utils import config


def read_dataset():
    """Read dataset and add 'Next GDP Growth' column
    Loads names of columns from indicators list in config
    Returns pandas dataset and names of features"""
    separator = "','"

    # Rename CountryCode to Country to make it easy to see the country names if needed
    sql_string = f""" SELECT t2.CountryCode as Country,
                    t1.Year, t3.IndicatorName,
                    t1.Value FROM CountryIndicators t1
                    LEFT JOIN
                    (SELECT ShortName as Country, CountryCode from Countries) t2
                    ON t1.CountryCode = t2.CountryCode
                    LEFT JOIN
                    (SELECT IndicatorCode, IndicatorName from Indicators)t3
                    ON t1.IndicatorCode = t3.IndicatorCode
                    WHERE t3.IndicatorName in ('{separator.join(config.INDICATORS)}');"""

    with sqlite3.connect(config.DATABASE_PATH) as conn:
        country_indicators_df = pd.read_sql(sql_string, conn)

    pivoted_df = country_indicators_df.pivot(
        values="Value", index=["Country", "Year"], columns=["IndicatorName"]
    )
    return pivoted_df, country_indicators_df


def retrieve_training_dataset(split):
    """Returns X/y_train/test and vector features using df created by read_dataset"""
    pivoted_df, country_indicators_df = read_dataset()

    features = pivoted_df.columns.tolist()

    target_df = country_indicators_df.loc[
        country_indicators_df["IndicatorName"] == config.GDP_GROWTH
    ].copy()
    target_df["Year"] -= 1
    target_df.set_index(["Country", "Year"], inplace=True)
    target_df.rename(columns={"Value": "Next GDP Growth"}, inplace=True)
    target_df.drop(columns=["IndicatorName"], inplace=True)

    df = pivoted_df.join(target_df)

    # Drop row if target is not present
    df = df.dropna(subset=[config.TARGET])

    X, y = df.iloc[:, :-1], df.iloc[:, -1]

    if split != 0:
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=split, random_state=1
        )
        return X_train, X_test, y_train, y_test, features

    return X, None, y, None, None


def retrieve_predict_dataset():
    """Return dataset to append predictions and X_predict to create them"""
    pivoted_df, _ = read_dataset()
    country_list = pivoted_df.index.unique("Country")

    # Dataframe with all the countries
    predictions = pd.DataFrame(country_list)
    predictions.rename(columns={"Country": "CountryCode"}, inplace=True)
    predictions["Year"] = config.NEXT_YEAR
    X_predict = pivoted_df.filter(like=f"{config.NEXT_YEAR}", axis=0)

    return predictions, X_predict


def write_predictions(predictions):
    with sqlite3.connect(config.DATABASE_PATH) as conn:
        predictions.to_sql("EstimatedGDPGrowth", conn, if_exists="replace", index=False)
