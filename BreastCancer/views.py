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
from .models import BreastCancer
import sqlite3

@csrf_exempt
def predicatBreastCancer(req):
    if req.method == 'POST':
        ###########Select the needed data from Database#########
        conn = sqlite3.connect("db.sqlite3")
        df= pd.read_sql_query("select * from BreastCancer_BreastCancer ;", conn)
        #########################################################
        if len(df)<=0:
            df = pd.read_csv('BreastCancer/dataset/data.csv')
            for i in range(len(df)):
                data=BreastCancer()
                data.Age=df.values[i][0]
                data.BMI=df.values[i][1]
                data.Glucose=df.values[i][2]
                data.Insulin=df.values[i][3]
                data.HOMA=df.values[i][4]
                data.Leptin=df.values[i][5]
                data.Adiponectin=df.values[i][6]
                data.Resistin=df.values[i][7]
                data.MCP=df.values[i][8]
                data.Classification=df.values[i][9]
                data.save()
            df = pd.read_csv('BreastCancer/dataset/data.csv')    
        
        body_unicode = req.body.decode('utf-8')
        body = json.loads(body_unicode)
        #  sample  that i want to to test it  that come from doctor
        sample = body['features']
        # get the data from dataset 
        # df = pd.read_csv('BreastCancer/dataset/data.csv')
        df.head()
        # determinde the features from the column (input)
        columns = ['Age', 'BMI', 'Glucose', 'Insulin', 'HOMA', 'Leptin', 'Adiponectin','Resistin', 'MCP']
        #  determinde the label (output) 
        label = df['Classification'].values
        features = df[list(columns)].values
        # config the data to be ready to train and test
        X_train, X_test, y_train, y_test = train_test_split(features, label, test_size = 0.3)
        #  use RandomForestClassifier algorthim
        clf = RandomForestClassifier(n_estimators = 50)
        # train the alg
        clf = clf.fit(X_train, y_train)
        clf = clf.fit(X_test, y_test)
        yprdicat = clf.predict([sample])
        # get the accurcy
        accurcy = clf.score(X_train, y_train)
        print(accurcy)
        print(yprdicat)
        data = {
            'predicate': int(yprdicat[0]),
            'accuracy' : float(accurcy * 100)
        }
        return JsonResponse (data, safe = False)
    else :
        return JsonResponse ('0', safe = False)
