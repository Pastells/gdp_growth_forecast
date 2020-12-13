"""Gradient Boosting Regressor from XGBoost"""
import sys

sys.path.append("..")

import logging
import numpy as np
from xgboost import XGBRegressor
from sklearn.metrics import r2_score, mean_squared_error
from utils import io


class GDPGrowthPredictor:
    """Gbm class"""

    def __init__(self, *args, **kwargs):
        """Create model with given parameters"""
        self.model = XGBRegressor(*args, **kwargs)

    def train(self, filename, split, *args, **kwargs):
        """Train model"""
        X_train, X_test, y_train, y_test, features = io.retrieve_training_dataset(split)
        self.model.fit(X_train, y_train, *args, **kwargs)
        self.save(filename)

        if split != 0:
            self.test(X_test, y_test, features, split)

    def test(self, X_test, y_test, features, split):
        """Test model"""
        model_y_pred = self.model.predict(X_test)

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

    def predict(self, filename, *args, **kwargs):
        """Make predictions for next year GDP growth,
        returns a pandas df"""
        self.load(filename)
        predictions, X_predict = io.retrieve_predict_dataset()
        predictions["Value"] = self.model.predict(X_predict, *args, **kwargs)
        return predictions

    def save(self, filename):
        """ Save model to file"""
        self.model.save_model(filename)
        logging.info("Model saved")

    def load(self, filename):
        """ Load model from file"""
        self.model.load_model(filename)
        logging.info("Model loaded")
