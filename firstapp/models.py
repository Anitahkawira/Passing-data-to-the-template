from django.db import models

# Create your models here.
class Student(models.Model):
    names = models.TextField()
    def __str__ (self):
        return self.names