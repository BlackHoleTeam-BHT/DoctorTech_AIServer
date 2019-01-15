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
from .models import HeartAttack
import json
import sqlite3



@csrf_exempt
def predicatHeartAttck(req):
            if req.method == 'POST':
                ###########Select the needed data from Database#########
                conn = sqlite3.connect("db.sqlite3")
                df= pd.read_sql_query("select * from HeartAttack_HeartAttack ;", conn)
                ###########Predict-HeartAttck###########################
                if len(df)<=0:
                    df=pd.read_csv('HeartAttack/dataset/Heart_Disease_Data.csv')
                    for i in range(len(df)):
                      data=HeartAttack()
                      data.age=df.values[i][0]
                      data.sex=df.values[i][1]
                      data.cp=df.values[i][2]
                      data.trestbps=df.values[i][3]
                      data.chol=df.values[i][4]
                      data.fbs=df.values[i][5]
                      data.restecg=df.values[i][6]
                      data.thalach=df.values[i][7]
                      data.exang=df.values[i][8]
                      data.oldpeak=df.values[i][9]
                      data.slop=df.values[i][10]
                      data.ca=df.values[i][11]
                      data.thal=df.values[i][12]
                      data.pred_attribute=df.values[i][13]
                      data.save()
                    df= pd.read_sql_query("select * from HeartAttack_HeartAttack ;", conn)  
                body_unicode = req.body.decode('utf-8')
                body = json.loads(body_unicode)
                #  sample  that i want to to test it  that come from doctor
                sample = body['features']
                print(sample)
                # get the data from dataset 
                df = pd.read_csv('HeartAttack/dataset/Heart_Disease_Data.csv')
                df.head()
                # determinde the features from the column (input)
                columns = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg','thalach', 'exang',
                           'oldpeak', 'slop', 'ca', 'thal']
                #  determinde the label (output) 
                # df['pred_attribute'].replace(inplace=True, value=[1, 1, 1, 1], to_replace=[1, 2, 3, 4])
                label = df['pred_attribute'].values
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
                data ={
                    'predicate': int(yprdicat[0]),
                    'accurcy' : float(accurcy)
                }
                return JsonResponse (data, safe = False)
            else :
                return JsonResponse ('0', safe = False)
