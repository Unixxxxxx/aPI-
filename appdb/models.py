from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    number = models.CharField(max_length=12)

    def __str__(self):
        return self.name 
