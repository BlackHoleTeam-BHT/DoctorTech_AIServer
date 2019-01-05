from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
import pandas as pd
import json
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse



#Note : this function use RandomForestClassifier algorithm to predict the diabetes result
@csrf_exempt 
def diabetesPredict(req):
    dataFrame=pd.read_csv('Diabetes/dataset/diabetes.csv')
    columns = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age']
    labels = dataFrame['Outcome'].values
    features = dataFrame[list(columns)].values
    X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.30)
    clf = RandomForestClassifier(n_estimators=10)
    clf = clf.fit(X_train, y_train)
    acurecy=clf.score(X_train,y_train)

    body_unicode = req.body.decode('utf-8')
    body = json.loads(body_unicode)
    Predict=clf.predict(body['value'])
    
    obj={}
    obj['result']=int(Predict[0])
    obj['acurecy']=float(acurecy)
    return JsonResponse(obj, safe=False)
     

