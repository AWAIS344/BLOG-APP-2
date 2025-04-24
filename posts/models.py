from django.db import models

# Create your models here.

class Tag(models.Model):
    name=models.CharField()


class Posts(models.Model):

    post_title=models.CharField(max_length=60)
    post_content=models.TextField()
    image=models.ImageField(upload_to='posts_images')
    updated_at =models.DateTimeField(auto_now=True)
    tag=models.ManyToManyField(Tag)

class Comment(models.Model):
    commment=models.TextField()
    post=models.ForeignKey(Posts,on_delete=models.CASCADE)


