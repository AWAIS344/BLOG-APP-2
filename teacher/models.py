from django.db import models

# Create your models here.

class Teacher(models.Model):

    name=models.CharField(max_length=50)
    email=models.EmailField()
    profile_image=models.ImageField(upload_to="teacher_images/")
    phone_number=models.IntegerField()
    bio=models.TextField()
    
