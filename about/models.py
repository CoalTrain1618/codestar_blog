from django.db import models

# Create your models here.

class About(models.Model):
    title = models.CharField(max_length=100,)
    content = models.TextField(max_length=700,)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title