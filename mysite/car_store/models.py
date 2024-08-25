from django.db import models

# Create your models here.
class Marka(models.Model):
    marka_name = models.CharField(max_length=16)

    def __str__(self):
        return self.marka_name
class Model(models.Model):
    model_name = models.CharField(max_length=26)
    markas = models.ForeignKey(Marka, on_delete=models.CASCADE)

    def __str__(self):
        return self.model_name
class Car(models.Model):
    car_name = models.CharField(max_length=22)
    description = models.TextField()
    year = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    color = models.CharField(max_length=16)
    volume = models.FloatField(default=0)
    modelkey = models.ForeignKey(Model, on_delete=models.CASCADE)
    markakey = models.ForeignKey(Marka, on_delete=models.CASCADE)

    def __str__(self):
        return self.car_name



