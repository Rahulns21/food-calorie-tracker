from django.db import models
from django.contrib.auth.models import User


class Food(models.Model):
    class Meta:
        verbose_name_plural = 'Food'

    def __str__(self) -> str:
        return self.name

    name = models.CharField(max_length=100)
    carbs = models.FloatField()
    protein = models.FloatField()
    fats = models.FloatField()
    calories = models.IntegerField()

class Consume(models.Model):
    class Meta:
        verbose_name_plural = 'Consumed'

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    food_consumed = models.ForeignKey(Food, on_delete=models.CASCADE)