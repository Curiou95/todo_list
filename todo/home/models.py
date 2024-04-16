from django.db import models

# Create your models here.
class To_do(models.Model):
    task = models.TextField()
    date = models.DateField(auto_now_add=True)
    status = models.IntegerField(default=0)
    