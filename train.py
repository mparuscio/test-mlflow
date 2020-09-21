# The data set used in this example is from http://archive.ics.uci.edu/ml/datasets/Wine+Quality
# P. Cortez, A. Cerdeira, F. Almeida, T. Matos and J. Reis.
# Modeling wine preferences by data mining from physicochemical properties. In Decision Support Systems, Elsevier, 47(4):547-553, 2009.

import os
import warnings
import sys
import random 

import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import ElasticNet
from urllib.parse import urlparse
import mlflow
import mlflow.sklearn

import logging

logging.basicConfig(level=logging.WARN)
logger = logging.getLogger(__name__)

if __name__ == "__main__":
      
    seed = float(sys.argv[1]) 
    random.seed(seed)
        
    with mlflow.start_run():
       
       # mlflow.log_param("seed", seed)
        

        file_name = 'artifact.txt'


        for i in range(10):
            accuracy = 1-random.random()/(i+1)
            mlflow.log_metric("accuracy", accuracy)
            f = open(file_name, 'a+')  # open file in append mode
            f.write('python rules : ' + str(accuracy) )
            f.close()
        
        mlflow.log_artifact("./"+str(file_name))
        #mlflow.sklearn.log_model(lr, "model")