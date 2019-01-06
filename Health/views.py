from django.shortcuts import render
from django.http import HttpResponse
from sklearn import linear_model
import pandas as pd 
from django.views.decorators.csrf import csrf_exempt
from .models import WeightHeight,CaloriesDistance
from django.http import JsonResponse
import sqlite3
import json


@csrf_exempt
def healthPredict(req):
    if req.method == 'POST':
      body_unicode = req.body.decode('utf-8')
      body = json.loads(body_unicode)      
      wight=body['wight']
      height=body['height']
      print(wight,height)
      ###########Select the needed data from Database#########
      conn = sqlite3.connect("db.sqlite3")
      dataFrameDC=pd.read_sql_query("select * from Health_CaloriesDistance ;", conn)
      dataFrameMW=pd.read_sql_query("select * from Health_WeightHeight ;", conn)
      ###########Distance-Calories#################################### 
      if len(dataFrameDC)<=0:
         dataFrameDC=pd.read_csv('Health/dataset/distanceCalories.csv')
         for i in range(len(dataFrameDC)):
             data=CaloriesDistance()
             data.Distance=dataFrameDC.values[i][0]
             data.Calories=dataFrameDC.values[i][1]
             data.save()
         dataFrameDC=pd.read_sql_query("select * from Health_CaloriesDistance ;", conn)   

      DC_target=dataFrameDC[['Distance']]
      DC_input=dataFrameDC[['Calories']]
      LinearDC=linear_model.LinearRegression()
      LinearDC.fit(DC_input,DC_target)
      AcurecyDC=LinearDC.score(DC_input, DC_target)
      print(LinearDC.predict([[500]]),AcurecyDC)
      ##########Minimum-Wight######################################### 
      if len(dataFrameMW)<=0:
         dataFrameMW=pd.read_csv('Health/dataset/heightweight.csv')
         for i in range(len(dataFrameMW)):
             data=WeightHeight()
             data.Height=dataFrameMW.values[i][0]
             data.Minimum=dataFrameMW.values[i][1]
             data.Maximum=dataFrameMW.values[i][2]
             data.save()
         dataFrameMW=pd.read_sql_query("select * from Health_WeightHeight ;", conn)   

      MW_target=dataFrameMW[['Minimum']]
      MW_input=dataFrameMW[['Height']]
      LinearMW=linear_model.LinearRegression()
      LinearMW.fit(MW_input,MW_target)
      AcurecyMW=LinearMW.score(MW_input, MW_target)
      print(LinearMW.predict([[160]]),AcurecyMW)
      ##########Maximum-Wight##########################################
      MM_target=dataFrameMW[['Maximum']]
      MM_input=dataFrameMW[['Height']]
      LinearMM=linear_model.LinearRegression()
      LinearMM.fit(MM_input,MM_target)
      AcurecyMM=LinearMM.score(MM_input, MM_target)
      print(LinearMM.predict([[160]]),AcurecyMM)
      #########Calculate The Result###################################
      MaxWight=LinearMM.predict([[height]])
      MinWight=LinearMW.predict([[height]])
      OverWight=wight-MaxWight[0][0]
      loseWight=MinWight[0][0]-wight
      calories= OverWight*3500/0.453
      distance=LinearDC.predict([[calories]])
      
      result={
          'MaxWight':MaxWight[0][0],
          'MinWight':MinWight[0][0],
          'OverWight':OverWight,
          'loseWight':loseWight,
          'calories':calories,
          'distance':distance[0][0]
      }
      print(result)
        


      return JsonResponse(result, safe=False)
    else:
      return JsonResponse('0', safe=False)   

