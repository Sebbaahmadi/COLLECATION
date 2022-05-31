from operator import truediv
from django.db import models

# Create your models here.
class Blogs (models.Model):
    title=models.CharField(max_length=200,null=True)
    text=models.TextField()
    data=models.DateTimeField()
    image=models.ImageField(upload_to="img/%y", null = True)

    def __str__(self):
        return self.title