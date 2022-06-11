import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report, ConfusionMatrixDisplay
from sklearn.preprocessing import MinMaxScaler
from sklearn.feature_selection import RFE
from sklearn.model_selection import train_test_split
import pickle

# load the model from disk
loaded_model = pickle.load(open('.\model\predict_ship_maintenance_new.sav', 'rb'))

#read in data file to predict
df = pd.read_csv('.\model\engFail.csv')

#Use loaded model
y_pred = loaded_model.predict(df)
#create new column and append predicted data for each engine
df['y'] = y_pred
#Only show engines that are predicted to require maintenance
df
#view data file content
print(df)
