from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    number = models.CharField(max_length=12)

    def __str__(self):
        return self.name 

class Service(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    button_text = models.CharField(max_length=50, default='Read More')
    button_link = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to='service_images/')  # needs Pillow installed

    def __str__(self):
        return self.title
