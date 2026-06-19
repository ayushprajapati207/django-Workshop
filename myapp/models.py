from django.db import models

# Create your models here.

class student(models.Model):
    name = models.CharField(max_length=30)
    mobile = models.IntegerField(max_length=10)
    email = models.EmailField()
    address = models.CharField()

    def __str__(self):
        return self.name
    
    

