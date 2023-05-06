from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    name = models.CharField(max_length = 100 , null= True)
    email = models.EmailField(unique= True, null = True)
    bio = models.TextField(null =True , blank = True)
    # avatar =

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

class Events(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null= True, blank = True )
    participants = models.ManyToManyField(User , blank= True)
    created = models.DateTimeField(auto_now_add=True)
    date = models.DateTimeField()
    updated = models.DateTimeField(auto_now =True)

    def __str__(self):
        return self.name
    
class submission(models.Model):
    participants = models.ForeignKey(User, on_delete=models.SET_NULL ,null=True)
    event = models.ForeignKey(Events,  on_delete= models.CASCADE)
    details  = models.TextField(null= True , blank = True)

    def __str__(self):
        return str(self.event ) + '---'+ str(self.participants)

