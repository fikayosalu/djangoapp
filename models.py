from django.db import models

# Create your models here.
class post(models.Model):
    title=models.CharField(max_length=200)
    author=models.ForeignKey('auth.user',on_delete=models.CASCADE)
    body=models.TextField()


    def __init__(self):
        return self.title



