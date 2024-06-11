from django.db import models

# Create your models here.
class School(models.Model):
    Sname=models.CharField(max_length=100,primary_key=True)
    Sage=models.PositiveIntegerField()
    Scollege=models.CharField(max_length=100)
    Slocation=models.CharField(max_length=100)
    
    def __str__(self):
        return self.Sname
    