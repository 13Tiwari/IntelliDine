# train.py
import pandas as pd
from sklearn.cluster import KMeans
from azureml.core import Run
import joblib

# Load preprocessed data
data = pd.read_csv('Backend/Data/CleanedData/cleaned_crime_data.csv')

# Train a KMeans clustering model
model = KMeans(n_clusters=5)
model.fit(data[['latitude', 'longitude']])

# Save the model
joblib.dump(model, 'crime_model.pkl')

# Log the model to the run
run = Run.get_context()
run.upload_file(name='outputs/crime_model.pkl', path_or_stream='crime_model.pkl')
run.complete()