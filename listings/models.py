from distutils.command.upload import upload
from django.db import models

class agents(models.Model):
    name=models.CharField(max_length=200)
    photo=models.ImageField(upload_to='agentphoto')
    description=models.TextField()
    phone=models.CharField(max_length=20)


    def __str__(self):
        return self.name

