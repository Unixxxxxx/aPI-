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

class Enquiry(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    work_email = models.EmailField(max_length=150)
    mobile_number = models.CharField(max_length=15)
    
    ENQUIRY_TYPES = [
        ('Corporate Travel', 'Corporate Travel'),
        ('Partnership', 'Partnership'),
        ('Support', 'Support'),
        ('Other', 'Other'),
    ]
    enquiry_type = models.CharField(max_length=50, choices=ENQUIRY_TYPES)
    
    message = models.TextField(blank=True, null=True)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.enquiry_type}"
