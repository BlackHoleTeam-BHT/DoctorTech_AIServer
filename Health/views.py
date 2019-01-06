from django.shortcuts import render
from django.http import HttpResponse
from sklearn import linear_model
import pandas as pd 
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
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
    MW_target=dataFrameMW[['minimum']]
    MW_input=dataFrameMW[['height ']]
    LinearMW=linear_model.LinearRegression()
    LinearMW.fit(MW_input,MW_target)
    AcurecyMW=LinearMW.score(MW_input, MW_target)
    print(LinearMW.predict([[160]]),AcurecyMW)
    ##########Maximum-Wight##########################################
    MM_target=dataFrameMW[['maximum ']]
    MM_input=dataFrameMW[['height ']]
    LinearMM=linear_model.LinearRegression()
    LinearMM.fit(MM_input,MM_target)
    AcurecyMM=LinearMM.score(MM_input, MM_target)
    print(LinearMM.predict([[160]]),AcurecyMM)



    return HttpResponse('1')

