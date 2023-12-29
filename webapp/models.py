from django.db import models

class employees(models.Model):
    fristname=models.CharField(max_length=10)
    lastname = models.CharField(max_length=10)
    emp_id=models.IntegerField()

    def __str__(self):
        return self.fristname
