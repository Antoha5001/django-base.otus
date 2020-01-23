from django.db import models

class StudentInformation(models.Model):

    firsr_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    card_number = models.CharField(max_length=10, unique=True)
    email = models.EmailField()

    def __str__(self):
        return f"{self.firsr_name} {self.last_name}"



# Create your models here.
