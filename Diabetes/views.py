from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split



#Note : this function use RandomForestClassifier algorithm to predict the diabetes result
def diabetesPredict(req):
    dataFrame=pd.read_csv('Diabetes/dataset/diabetes.csv')
    columns = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age']
    labels = dataFrame['Outcome'].values
    for i in range(8):
        print(dataFrame.values[i])
    print(len(dataFrame))
    return HttpResponse('<p>eeee</p>')
     

