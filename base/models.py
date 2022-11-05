from django.db import models

# Create your models here.


class Operation(models.Model):
    operation_type = models.CharField(max_length = 255)
    x = models.IntegerField()
    y = models.IntegerField()

