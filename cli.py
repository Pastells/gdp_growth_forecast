#!/usr/bin/env python
"""Main program
Predict next year GDP Growth from a kaggle database
Narcís Font, Pol Pastells
December 2020
"""
import os
import sys
import time
import logging
import argparse
from datetime import datetime
from utils import config, models, _io


time_file = datetime.now().strftime("cli_%Y-%m-%d_%H:%M:%S.log")

logging.basicConfig(
    filename=os.path.join(config.LOGS_PATH, time_file),
    format="%(asctime)s - [%(levelname)s] - %(message)s",
    level=logging.INFO,
)


def log_print_func():
    """print all the logging info"""
    root = logging.getLogger()
    root.setLevel(logging.DEBUG)

    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    handler.setFormatter(formatter)
    root.addHandler(handler)


parser = argparse.ArgumentParser(description="Predict next year GDP growth")
parser.add_argument(
    "task",
    choices=["train", "predict"],
    help="Task to be performed",
)
parser.add_argument(
    "-split",
    type=float,
    default=0.3,
    help="test size in test-train split. Domain: (0,1) + {0}. \
    If set to 0 no split is made.",
)
parser.add_argument(
    "-filename",
    type=str,
    default="XGBoost.model",
    help="Name for the model to be saved/loaded",
)
parser.add_argument(
    "-previous_year",
    action="store_true",
    help="specify to use data from 2 years. \
            If wanted, must be used in both training and predict",
)
parser.add_argument("-log_print", action="store_true", help="specify to print log")


if __name__ == "__main__":
    args = parser.parse_args()
    if args.log_print:
        log_print_func()

    filename = os.path.join(config.MODELS_PATH, args.filename)

    if args.task == "train":
        logging.info("Training")
        t0 = time.time()
        try:
            model = models.GDPGrowthPredictor(**config.XG_PARAMS)
            model.train(filename, args.split, args.previous_year)
            logging.info("Elapsed time: %.3f seconds", time.time() - t0)
        except:
            logging.exception("Error while training")
            raise

    if args.task == "predict":
        logging.info("Predicting")
        t0 = time.time()
        try:
            model = models.GDPGrowthPredictor(**config.XG_PARAMS)
            predictions = model.predict(filename, args.previous_year)
            _io.write_predictions(predictions)
            logging.info("Predictions saved into database")
            logging.info("Elapsed time: %.3f seconds", time.time() - t0)
        except:
            logging.exception("Error while predicting")
            raise
