from django.db import models

# Create your models here.

class About(models.Model):
    title = models.CharField(max_length=100,)
    content = models.TextField(max_length=300)
    updated_on = models.DateTimeField(auto_add=True)

    def __str__(self):
        return self.title