from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix

import json

@csrf_exempt
def predicatBreastCancer(req):
    if req.method == 'POST':
        body_unicode = req.body.decode('utf-8')
        body = json.loads(body_unicode)
        #  sample  that i want to to test it  that come from doctor
        sample = body.features
        # get the data from dataset 
        df = pd.read_csv('BreastCancer/dataset/data.csv')
        df.head()
        # determinde the features from the column (input)
        columns = ['Age', 'BMI', 'Glucose', 'Insulin', 'HOMA', 'Leptin', 'Adiponectin','Resistin', 'MCP.1']
        #  determinde the label (output) 
        label = df['Classification'].values
        features = df[list(columns)].values
        # config the data to be ready to train and test
        X_train, X_test, y_train, y_test = train_test_split(features, label, test_size = 0.3)
        #  use RandomForestClassifier algorthim
        clf = RandomForestClassifier(n_estimators= 50)
        # train the alg
        clf = clf.fit(X_train, y_train)
        clf = clf.fit(X_test, y_test)
        yprdicat = clf.predict([sample])
        # get the accurcy
        accurcy = clf.score(X_train, y_train)
        print(accurcy)
        print(yprdicat)
        
        return HttpResponse-(body)