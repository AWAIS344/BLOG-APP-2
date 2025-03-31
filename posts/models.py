from django.db import models

# Create your models here.

class Posts(models.Model):

    post_title=models.CharField(max_length=60)
    post_content=models.TextField()
    updated_at =models.DateTimeField(auto_now=True)