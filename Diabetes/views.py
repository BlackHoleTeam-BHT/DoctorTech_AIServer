from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
import pandas as pd
import json
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import Diabetes
import sqlite3


# Note : this function use RandomForestClassifier algorithm to predict the diabetes result
@csrf_exempt
def diabetesPredict(req):
    if req.method == 'POST':
        ###########Select the needed data from Database#########
        conn = sqlite3.connect("db.sqlite3")
        dataFrame= pd.read_sql_query("select * from Diabetes_Diabetes ;", conn)
        ###########Predict-Diabetes#############################
        if len(dataFrame)<=0:
            dataFrame=pd.read_csv('Diabetes/dataset/diabetes.csv')
            for i in range(len(dataFrame)):
              data=Diabetes()
              data.Pregnancies=dataFrame.values[i][0]
              data.Glucose=dataFrame.values[i][1]
              data.BloodPressure=dataFrame.values[i][2]
              data.SkinThickness=dataFrame.values[i][3]
              data.Insulin=dataFrame.values[i][4]
              data.BMI=dataFrame.values[i][5]
              data.DiabetesPedigreeFunction=dataFrame.values[i][6]
              data.Age=dataFrame.values[i][7]
              data.Outcome=dataFrame.values[i][8]
              data.save()
            dataFrame= pd.read_sql_query("select * from Diabetes_Diabetes ;", conn)  

        columns = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness',
                   'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age']
    #   labels = dataFrame['Outcome'].values
        labels = dataFrame['Outcome'].values
        features = dataFrame[list(columns)].values
    #   features = dataFrame[list(columns)].values
        X_train, X_test, y_train, y_test = train_test_split(
            features, labels, test_size=0.30)
        clf = RandomForestClassifier(n_estimators=15)
        clf = clf.fit(X_train, y_train)
        acurecy = clf.score(X_train, y_train)

        body_unicode = req.body.decode('utf-8')
        body = json.loads(body_unicode)
        Predict = clf.predict(body['value'])

        obj = {}
        obj['result'] = int(Predict[0])
        obj['acurecy'] = float(acurecy)
        return JsonResponse(obj, safe=False)

    else:
        return JsonResponse('0', safe=False)
