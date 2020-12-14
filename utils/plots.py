"""Plots"""
import os
from matplotlib import pyplot as plt
from sklearn.metrics import r2_score
import shap
from . import config


def plot_performance_results(y_real, y_pred):
    """Model performance: Plot real vs pedicted values"""

    fig, ax = plt.subplots()
    plot_range = [y_real.min(), y_real.max()]
    ax.set_title("Model performance")
    ax.set_ylabel("Pred value")
    ax.set_xlabel("Real value")
    ax.scatter(y_real, y_pred, s=4)
    ax.plot(plot_range, plot_range, c="red")
    plt.xlim((-15, 15))
    plt.ylim((-15, 15))
    plt.grid()
    plt.annotate("R^2 = {:.3f}".format(r2_score(y_real, y_pred)), (-14, 13))
    filename = os.path.join(config.LOGS_PATH, "model_performance.png")
    plt.savefig(filename)
    plt.close()


def plot_shap_results(X_test, features, gbm_model):
    """Shap plots"""

    shap.initjs()
    explainer = shap.TreeExplainer(gbm_model)
    shap_values = explainer.shap_values(X_test)

    fig1 = shap.summary_plot(shap_values, X_test, feature_names=features, show=False)
    filename = os.path.join(config.MODELS_PATH, "shap_impact_on_model_output.pdf")
    plt.savefig(
        filename,
        format="pdf",
        dpi=1000,
        bbox_inches="tight",
    )
    plt.close()

    fig2 = shap.summary_plot(
        shap_values, X_test, plot_type="bar", feature_names=features, show=False
    )
    filename = os.path.join(
        config.MODELS_PATH, "shap_average_impact_on_model_output_magnitude.pdf"
    )
    plt.savefig(
        filename,
        format="pdf",
        dpi=1000,
        bbox_inches="tight",
    )
