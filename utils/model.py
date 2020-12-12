"""Gradient Boosting Regressor from XGBoost"""
from xgboost import XGBRegressor


class GDPGrowthPredictor:
    """Gbm class"""

    def __init__(self, *args, **kwargs):
        """Create model with given parameters"""
        self.model = XGBRegressor(*args, **kwargs)

    def train(self, X_train, y_train, *args, **kwargs):
        """Train model"""
        self.model.fit(X_train, y_train, *args, **kwargs)

    def predict(self, X_test, *args, **kwargs):
        """Predict"""
        y_prediction = self.model.predict(X_test, *args, **kwargs)
        return y_prediction

    @staticmethod
    def load(filename):
        pass

    def save(self, filename):
        pass
