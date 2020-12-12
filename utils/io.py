"""Read and write into dataset"""

import sqlite3
import pandas as pd
from utils import config


def read_dataset():
    """Read dataset and add 'Next GDP Growth' column"""
    indicators = config.INDICATORS
    target = config.TARGET
    gdp = config.GDP_GROWTH
    separator = "','"
    sql_string = f""" SELECT t2.Country,
                    t1.Year, t3.IndicatorName,
                    t1.Value FROM CountryIndicators t1
                    LEFT JOIN
                    (SELECT ShortName as Country, CountryCode from Countries) t2
                    ON t1.CountryCode = t2.CountryCode
                    LEFT JOIN
                    (SELECT IndicatorCode, IndicatorName from Indicators)t3
                    ON t1.IndicatorCode = t3.IndicatorCode
                    WHERE t3.IndicatorName in ('{separator.join(indicators)}');"""

    with sqlite3.connect(config.DATABASE_PATH) as conn:
        country_indicators_df = pd.read_sql(sql_string, conn)

    pivoted_df = country_indicators_df.pivot(
        values="Value", index=["Country", "Year"], columns=["IndicatorName"]
    )

    features = pivoted_df.columns.tolist()

    target_df = country_indicators_df.loc[
        country_indicators_df["IndicatorName"] == gdp
    ].copy()
    target_df["Year"] -= 1
    target_df.set_index(["Country", "Year"], inplace=True)
    target_df.rename(columns={"Value": "Next GDP Growth"}, inplace=True)
    target_df.drop(columns=["IndicatorName"], inplace=True)
    df = pivoted_df.join(target_df)

    df = df.dropna(subset=[target])  # Drop row if target is not present

    return df, features


def retrieve_training_dataset():
    pass


def retrieve_predict_dataset():
    pass
