from django.db import models

# Create your models here.
class Students(models.Model):
    name=models.CharField(max_length=10)
    roll_no=models.IntegerField()
    age=models.IntegerField()

    def __str__(self):
        return self.name
