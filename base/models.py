from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    name = models.CharField(max_length = 100 , null= True) # the datasets are given for the name  
    email = models.EmailField(unique= True, null = True)#  the datasers that are given in the email field 
    bio = models.TextField(null =True , blank = True) # the databse that handles the the bio field 
    # creawting databases that are given in the code base 


    hackathon_participants = models.BooleanField(default = True , null = True)
    # avatar =

    USERNAME_FIELD = 'email' # usigng the usernames as emails for the login pages
    REQUIRED_FIELDS = ['username'] # using the required fields as names

# data bases for users to have events in the hackathon
class Events(models.Model):
    name = models.CharField(max_length=200) # datasets for names in the events 
    description = models.TextField(null= True, blank = True ) # datasets for the description in the events 
    participants = models.ManyToManyField(User , blank= True) # dataset for viewing the description inthe events 
    created = models.DateTimeField(auto_now_add=True) #for adding time stamps
    date = models.DateTimeField() # for viewing the time the user created the events
    updated = models.DateTimeField(auto_now =True) # for viewing the updated 

    def __str__(self):
        return self.name # returning the string name of the events 
    
class submission(models.Model):
    participants = models.ForeignKey(User, on_delete=models.SET_NULL ,null=True) #datasets for patitcipants to submit the event registered 
    event = models.ForeignKey(Events,  on_delete= models.CASCADE)# to know the events you are submitting 
    details  = models.TextField(null= True , blank = True)# the details about the user for the submission

    def __str__(self):
        return str(self.event ) + '---'+ str(self.participants)

