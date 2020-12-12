"""Main program"""

import sys

sys.path.append("..")

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error
from utils import config
from utils import io
import utils.model

print("creating dataset")
df, features = io.read_dataset()

X, y = df.iloc[:, :-1], df.iloc[:, -1]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)

print("creating model")
model = utils.model.GDPGrowthPredictor(**config.XG_PARAMS)
model.train(X_train, y_train)
model_y_pred = model.predict(X_test)

results_df = X_test
results_df = results_df.drop(columns=features)
results_df["y_real"] = y_test
results_df["y_pred"] = model_y_pred
results_df["err"] = np.absolute(results_df["y_real"] - results_df["y_pred"])
results_df["%_err"] = (results_df["err"]) / (np.absolute(results_df["y_real"])) * 100

print(f"RMSE: {mean_squared_error(y_test, model_y_pred)**0.5}")
print(f"R^2: {r2_score(y_test, model_y_pred)}")

raise ValueError("Error on purpose, following code is not tested")

# Predicted Value Plot

fig, ax = plt.subplots()
plot_range = [results_df["y_real"].min(), results_df["y_real"].max()]
ax.set_title("Model performance")
ax.set_ylabel("Pred value")
ax.set_xlabel("Real value")

ax.scatter(results_df["y_real"], results_df["y_pred"], s=4)
ax.plot(plot_range, plot_range, c="red")
plt.show()


# We have to make the predict for the year 2010, using the last indicators info
# And write the info on the data-base

country_list = df.index.unique("Country")
country_list

# Last indicators information #Utilitzo el pivoted perque no estan modificats els anys
pivoted_df = pivoted_df.dropna(axis="columns", thresh=6000)
pivoted_df = pivoted_df.dropna()
pivoted_df.drop(columns=["GDP growth (annual %)"], inplace=True)
pivoted_df

# Dataframe with all the countries
results_test = pd.DataFrame(country_list)

# Array to save all the predicted values of the last year
Predicted_values = np.array([])
# We will have to add the prediction function
for country in country_list:
    pred_indicators = pivoted_df.loc[country].iloc[
        [-1]
    ]  # Select last row of each contry,
    xg_reg_y_pred = xg_reg.predict(pred_indicators)
    Predicted_values = np.append(Predicted_values, xg_reg_y_pred)

results_test["GDP Growth Prediciton ( Year 2010 )"] = Predicted_values
