"""Paths and constants for gdp growth project"""
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATABASE_PATH = os.path.join(BASE_DIR, "db.sqlite3")

MODELS_PATH = os.path.join(BASE_DIR, "models")

LOGS_PATH = os.path.join(BASE_DIR, "logs")

GDP_GROWTH = "GDP growth (annual %)"

TARGET = "Next GDP Growth"

XG_PARAMS = {
    "objective": "reg:squarederror",
    "colsample_bytree": 0.3,
    "learning_rate": 0.1,
    "max_depth": 7,
    "n_estimators": 40,
    "alpha": 50,  # L1 regularization
    "lambda": 15,  # L2 regularization
}

INDICATORS = [
    "GDP growth (annual %)",
    "Adjusted savings: education expenditure (% of GNI)",
    "GDP per capita growth (annual %)",
    "Population growth (annual %)",
    "Industry, value added (annual % growth)",
    "Services, etc., value added (annual % growth)",
    "Urban population growth (annual %)",
    "Exports of goods and services (annual % growth)",
    "GNI growth (annual %)",
    "Foreign direct investment, net inflows (% of GDP)",
    "Mobile cellular subscriptions",
    "Food production index (2004-2006 = 100)",
    "Hospital beds (per 1,000 people)",
    "GNI per capita, Atlas method (current US$)",
    "Short-term debt (% of total reserves)",
    "Inflation, consumer prices (annual %)",
    "Livestock production index (2004-2006 = 100)",
    "Fixed telephone subscriptions (per 100 people)",
    "GDP per capita (current US$)",
    "External balance on goods and services (current LCU)",
    "S&P Global Equity Indices (annual % change)",
    "Agriculture, value added (annual % growth)",
    "Labor force participation rate, male (% of male population ages 15-64) (modeled ILO estimate)",
    "Adjusted net national income per capita (current US$)",
    "PPP conversion factor, GDP (LCU per international $)",
    "Newborns protected against tetanus (%)",
    "Inflation, GDP deflator (annual %)",
    "Crop production index (2004-2006 = 100)",
    "Total reserves minus gold (current US$)",
    "Death rate, crude (per 1,000 people)",
    "Population in largest city",
    "Mortality rate, adult, male (per 1,000 male adults)",
    "Final consumption expenditure, etc. (annual % growth)",
    "Age dependency ratio, old (% of working-age population)",
    "Total reserves (% of total external debt)",
    "Currency composition of PPG debt, French franc (%)",
    "Net official flows from UN agencies, UNICEF (current US$)",
    "Survival to age 65, male (% of cohort)",
    "Grants, excluding technical cooperation (BoP, current US$)",
    "School enrollment, secondary (% gross)",
    "Adjusted net savings, excluding particulate emission damage (% of GNI)",
    "International migrant stock, total",
    "Rural population growth (annual %)",
    "External balance on goods and services (current US$)",
    "Life expectancy at birth, total (years)",
    "GDP per capita (current LCU)",
    "CO2 emissions (kg per 2005 US$ of GDP)",
    "Household final consumption expenditure (annual % growth)",
    "Merchandise exports to developing economies in South Asia (% of total merchandise exports)",
    "Life expectancy at birth, male (years)",
]
