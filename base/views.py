from django.shortcuts import render
from .models import User , Events , submission

# Create your views here.
def homepage(request):
    users = User.objects.filter(hackathon_participants = True) # to filter users using the events only 
    events = Events.objects.all() # to gets all events registered in the database 
    context = {'users': users , 'events': events}
    return render(request  , 'home.html',context)

def events_page(request , pk):
    event = Events.objects.get(id = pk)
    context = {'event':event}
    return render(request, 'events.html', context)


def registration_confirm(request):
    pass