from django.shortcuts import render
from django.http import HttpResponse
from sklearn import linear_model
import pandas as pd 



def healthPredict(req):
    ###########Distance-Calories####################################
    dataFrameDC=pd.read_csv('Health/dataset/distanceCalories.csv')
    DC_target=dataFrameDC[['distance']]
    DC_input=dataFrameDC[['calories']]
    LinearDC=linear_model.LinearRegression()
    LinearDC.fit(DC_input,DC_target)
    AcurecyDC=LinearDC.score(DC_input, DC_target)
    print(LinearDC.predict([[500]]),AcurecyDC)
    ##########Minimum-Wight######################################### 
    dataFrameMW=pd.read_csv('Health/dataset/heightweight.csv')
    print(dataFrameMW)
    MW_target=dataFrameMW[['minimum']]
    MW_input=dataFrameMW[['height ']]
    LinearMW=linear_model.LinearRegression()
    LinearMW.fit(MW_input,MW_target)
    AcurecyMW=LinearMW.score(MW_input, MW_target)
    print(LinearMW.predict([[160]]),AcurecyMW)


    return HttpResponse('1')

