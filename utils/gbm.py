"""Train gbm model"""

import sys

sys.path.append("..")

import numpy as np
from sklearn.metrics import r2_score, mean_squared_error
from utils import config
from utils import io
import utils.model


def gbm_train(filename, split):
    X_train, y_train = io.retrieve_training_dataset(split)
    model = utils.model.GDPGrowthPredictor(**config.XG_PARAMS)
    model.train(X_train, y_train)
    model.save(filename)


def gbm_test(filename, split):
    model = utils.model.GDPGrowthPredictor(**config.XG_PARAMS)
    model.load(filename)
    X_test, y_test, features = io.retrieve_predict_dataset(split)
    model_y_pred = model.predict(X_test)

    results_df = X_test
    results_df = results_df.drop(columns=features)
    results_df["y_real"] = y_test
    results_df["y_pred"] = model_y_pred
    results_df["err"] = np.absolute(results_df["y_real"] - results_df["y_pred"])
    results_df["%_err"] = (
        (results_df["err"]) / (np.absolute(results_df["y_real"])) * 100
    )

    print(f"RMSE: {mean_squared_error(y_test, model_y_pred)**0.5}")
    print(f"R^2: {r2_score(y_test, model_y_pred)}")
