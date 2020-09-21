from django.db import models

# Create your models here.
class Content(models.Model):
    contents_url=models.CharField(max_length=200)
    contents_name=models.CharField(max_length=100)
    contents_image=models.CharField(max_length=200)


    def __str__(self):
        return self.contents_name