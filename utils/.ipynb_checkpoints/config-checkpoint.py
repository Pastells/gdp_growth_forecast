import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATABASE_PATH = os.path.join(BASE_DIR, "db.sqlite3") 

MODELS_PATH = os.path.join(BASE_DIR, "models")

LOGS_PATH = os.path.join(BASE_DIR, "logs")

GDP_GROWTH = "GDP growth (annual %)"
TARGET = "Next GDP Growth"


INDICATORS = ['GDP growth (annual %)',
 'GDP per capita growth (annual %)',
 'Industry, value added (annual % growth)',
 'Services, etc., value added (annual % growth)',
 'Population growth (annual %)',
 'GNI growth (annual %)',
 'Adjusted net national income per capita (current US$)',
 'Urban population growth (annual %)',
 'Inflation, consumer prices (annual %)',
 'GNI per capita, Atlas method (current US$)',
 'Livestock production index (2004-2006 = 100)',
 'Imports of goods and services (annual % growth)',
 'Adjusted savings: education expenditure (% of GNI)',
 'GDP per capita (current US$)',
 'S&P Global Equity Indices (annual % change)',
 'Mobile cellular subscriptions',
 'Total reserves (% of total external debt)',
 'Foreign direct investment, net inflows (BoP, current US$)',
 'General government final consumption expenditure (annual % growth)',
 'Short-term debt (% of total reserves)',
 'Exports of goods and services (annual % growth)',
 'Death rate, crude (per 1,000 people)',
 'PPP conversion factor, GDP (LCU per international $)',
 'Foreign direct investment, net inflows (% of GDP)',
 'GDP per unit of energy use (PPP $ per kg of oil equivalent)',
 'Newborns protected against tetanus (%)',
 'Agriculture, value added (annual % growth)',
 'Adjusted net national income (annual % growth)',
 'Health expenditure per capita (current US$)',
 'Population in largest city',
 'Export value index (2000 = 100)',
 'External balance on goods and services (% of GDP)',
 'Food production index (2004-2006 = 100)',
 'Life expectancy at birth, female (years)',
 'Crop production index (2004-2006 = 100)',
 'Merchandise trade (% of GDP)',
 'CO2 emissions (kt)',
 'External balance on goods and services (current LCU)',
 'Import value index (2000 = 100)',
 'Mobile cellular subscriptions (per 100 people)',
 'Labor force participation rate, male (% of male population ages 15-64) (modeled ILO estimate)',
 'Net current transfers from abroad (current US$)',
 'Life expectancy at birth, male (years)',
 'Export volume index (2000 = 100)',
 'GDP deflator (base year varies by country)',
 'Imports of goods and services (% of GDP)',
 'Total reserves minus gold (current US$)',
 'Adjusted savings: net national savings (% of GNI)',
 'International migrant stock, total']



INDICATORS_old = [
    "GDP growth (annual %)",
    "GDP per capita growth (annual %)",
    "Population growth (annual %)",
    "General government final consumption expenditure (% of GDP)",
    "Inflation, GDP deflator (annual %)",
    "Rural population growth (annual %)",
    "Urban population growth (annual %)",
    "GNI growth (annual %)",
    "Population ages 0-14 (% of total)",
    "Population ages 15-64 (% of total)",
    "Population ages 65 and above (% of total)",
    "Population density (people per sq. km of land area)",
    "Population in largest city",
    "Population in the largest city (% of urban population)",
    "Population in urban agglomerations of more than 1 million",
    "Population in urban agglomerations of more than 1 million (% of total population)",
    "Rural population",
    "Rural population (% of total population)",
    "Urban population",
    "Urban population (% of total)",
    "Foreign direct investment, net inflows (% of GDP)",
    "Foreign direct investment, net outflows (% of GDP)",

]
