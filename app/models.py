from django.db import models

# Create your models here.
class Students(models.Model):
    username = models.CharField(max_length=20)
    fullname = models.CharField(max_length=30)
    email = models.CharField(max_length=40)
    phone_number = models.IntegerField()
    profilepic = models.ImageField(upload_to="img",blank=True,null=True)
def __str__(self):
    return self.username
