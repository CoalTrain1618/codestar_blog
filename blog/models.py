from django.db import models
from django.contrib.auth.models import User

# Create your models here.

STATUS = ((0, "Draft"), (1, "Published"))

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True) # Only accepts python sting data with the use of .CharField
    slug = models.SlugField(max_length=200, unique=True) # SlugField is used for URL-friendly representation of the title
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    ) # ForeignKey creates a many-to-one relationship with the User model.
    content = models.TextField() # TextField is used for large text content box.
    created_on = models.DateTimeField(auto_now_add=True) # DateTimeField automatically sets the date and time when the post is created.
    status = models.IntegerField(choices=STATUS, default=0) # IntegerField is used to store the status of the post, with choices defined in STATUS tuple.
    excerpt =  models.TextField(max_length=200, blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ["-created_on"]
    def __str__(self):
        return f"{self.title}| Written by {self.author}" 

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="commenter")
    body = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ["created_on"]
    def __str__(self):
        return f"{self.body} by {self.author}"