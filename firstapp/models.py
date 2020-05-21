from django.db import models

# Create your models here.
class School(models.Model):
    name = models.CharField(max_length = 20)
    address = models.CharField(max_length = 40)

    def __str__(self):
        return self.name