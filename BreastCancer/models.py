from django.db import models

# Create your models here.
class BreastCancer (models.Model):
    Age = models.DecimalField(max_digits=10, decimal_places=4)
    BMI = models.DecimalField(max_digits=10, decimal_places=4)
    Glucose = models.DecimalField(max_digits=10, decimal_places=4)
    Insulin =  models.DecimalField(max_digits=10, decimal_places=4)
    HOMA = models.DecimalField(max_digits=10, decimal_places=4)
    Leptin = models.DecimalField(max_digits=10, decimal_places=4)
    Adiponectin = models.DecimalField(max_digits=10, decimal_places=4)
    Resistin = models.DecimalField(max_digits=10, decimal_places=4)
    MCP = models.DecimalField(max_digits=10, decimal_places=4)
    Classification = models.DecimalField(max_digits=10, decimal_places=4)