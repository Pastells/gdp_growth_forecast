## GDP Growth Forecast

Authors: Pol Pastells Vilà, Narcís Font Massot (December 2020)

Python project for a master's course (see project\_description):

Predicting the GDP Growth for the next year using the World Development Indicators with SQL from Kaggle:

https://www.kaggle.com/mariapushkareva/world-development-indicators-with-sql

Actually, we used a slightly different version, with data only till 2010, and the objective was to predict the 2011 GDP growth.

### Execution

For the program to work, unzip the database and leave it in the same folder as cli.py.

We used a virtualenv to run the program, all the dependencies can be found inside requirements.txt.

### Structure

The folders are structured as follows:

+ Analysis: contains notebooks to document the process and the final model explained.

+ Logs: folder where logging saves the logs of the program.

+ Models: folder to save the model and created plots.

+ Reports: html version of the notebooks.

+ Utils: modules called from cli.py (main program)


