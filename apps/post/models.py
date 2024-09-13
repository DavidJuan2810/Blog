from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=600)
    order = models.IntegerField()
    created_ad = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title