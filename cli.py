#!/usr/bin/env python
import os
import time
import logging
import argparse
from datetime import datetime
from utils import config, io, model, gbm


time_file = datetime.now().strftime("cli_%Y-%m-%d_%H:%M:%S")

logging.basicConfig(
    filename=os.path.join(config.LOGS_PATH, time_file) + ".log",
    format="%(asctime)s - [%(levelname)s] - %(message)s",
    level=logging.INFO,
)

filename = os.path.join(config.MODELS_PATH, time_file) + ".model"

parser = argparse.ArgumentParser(description="Predict next year GDP growth")
parser.add_argument(
    "task",
    choices=["train", "predict"],
    help="Task to be performed",
)
parser.add_argument(
    "-split",
    type=float,
    default=0.7,
    help="test size in test-train split. Domain: (0,1) + {0}. \
    If set to 0 no split is made.",
)


if __name__ == "__main__":
    args = parser.parse_args()
    if args.task == "train":
        logging.info("Training")
        t0 = time.time()
        gbm.gbm_train(filename, args.split)
        logging.info("Elapsed time training/testing: %.3f seconds", time.time() - t0)

    if args.task == "predict":
        logging.info("Predicting")
