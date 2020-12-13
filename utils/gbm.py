"""Train/test/predict using gbm model"""

import sys

sys.path.append("..")

import logging
import numpy as np
from sklearn.metrics import r2_score, mean_squared_error
from utils import config
from utils import io
import utils.model


def gbm_train(filename, split):
    """Train model"""
    X_train, X_test, y_train, y_test, features = io.retrieve_training_dataset(split)
    model = utils.model.GDPGrowthPredictor(**config.XG_PARAMS)
    model.train(X_train, y_train)
    model.save(filename)

    if split != 0:
        gbm_test(model, X_test, y_test, features, split)


def gbm_test(model, X_test, y_test, features, split):
    """Test model"""
    model_y_pred = model.predict(X_test)

    results_df = X_test
    results_df = results_df.drop(columns=features)
    results_df["y_real"] = y_test
    results_df["y_pred"] = model_y_pred
    results_df["err"] = np.absolute(results_df["y_real"] - results_df["y_pred"])
    results_df["%_err"] = (
        (results_df["err"]) / (np.absolute(results_df["y_real"])) * 100
    )

    logging.info("Test results with %s split:", split)
    logging.info("\t RMSE: %.3f", mean_squared_error(y_test, model_y_pred) ** 0.5)
    logging.info("\t R^2: %.3f", r2_score(y_test, model_y_pred))


def gbm_predict(filename):
    """Make predictions for next year GDP growth"""
    pass
