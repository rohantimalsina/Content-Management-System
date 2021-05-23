from django.db import models

class Contact(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    subject=models.TextField()
    message=models.TextField()
    def __str_(self):
        return self.mail