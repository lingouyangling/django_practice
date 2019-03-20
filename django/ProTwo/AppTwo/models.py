from django.db import models

# Create your models here.
class User(models.Model):
    fname = models.CharField(max_length=264)
    lname = models.CharField(max_length=264)
    email = models.EmailField(max_length=264)

    def __str__(self):
        return self.fname+ ' ' + self.lname
