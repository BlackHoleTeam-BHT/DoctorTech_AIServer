from django.db import models



class WeightHeight(models.Model):
    Height=models.DecimalField(max_digits=10, decimal_places=4)
    Minimum=models.DecimalField(max_digits=10, decimal_places=4)
    Maximum =models.DecimalField(max_digits=10, decimal_places=4)


class CaloriesDistance(models.Model):
    Calories=models.DecimalField(max_digits=10, decimal_places=4)
    Distance=models.DecimalField(max_digits=10, decimal_places=4)
