from django.db import models

class Diabetes(models.Model):
    Pregnancies=models.DecimalField(max_digits=10, decimal_places=4)
    Glucose=models.DecimalField(max_digits=10, decimal_places=4)
    BloodPressure=models.DecimalField(max_digits=10, decimal_places=4)
    SkinThickness=models.DecimalField(max_digits=10, decimal_places=4)
    Insulin=models.DecimalField(max_digits=10, decimal_places=4)
    BMI=models.DecimalField(max_digits=10, decimal_places=4)
    DiabetesPedigreeFunction=models.DecimalField(max_digits=10, decimal_places=4)
    Age=models.DecimalField(max_digits=10, decimal_places=4)
    Outcome=models.DecimalField(max_digits=10, decimal_places=4)

