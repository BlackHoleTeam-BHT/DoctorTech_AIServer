from django.db import models

class HeartAttack(models.Model):
    age=models.DecimalField(max_digits=10, decimal_places=4)
    sex=models.DecimalField(max_digits=10, decimal_places=4)
    cp=models.DecimalField(max_digits=10, decimal_places=4)
    trestbps=models.DecimalField(max_digits=10, decimal_places=4)
    chol=models.DecimalField(max_digits=10, decimal_places=4)
    fbs=models.DecimalField(max_digits=10, decimal_places=4)
    restecg=models.DecimalField(max_digits=10, decimal_places=4)
    thalach=models.DecimalField(max_digits=10, decimal_places=4)
    exang=models.DecimalField(max_digits=10, decimal_places=4)
    oldpeak=models.DecimalField(max_digits=10, decimal_places=4)
    slop=models.DecimalField(max_digits=10, decimal_places=4)
    ca=models.DecimalField(max_digits=10, decimal_places=4)
    thal=models.DecimalField(max_digits=10, decimal_places=4)
    pred_attribute=models.DecimalField(max_digits=10, decimal_places=4)