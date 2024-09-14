import pandas as pd 
from DataCleaner import clean_data
from azureml.core import Workspace, Experiment, ScriptRunConfig, Environment
from azureml.core import Run
from sklearn.cluster import KMeans
import joblib

#Uncomment to clean additional data
#clean_data('crime_data.csv')

ws = Workspace.from_config(path='config.json')
#print(ws.name, ws.resource_group, ws.location, ws.subscription_id, sep = '\n')
