from django.shortcuts import render, redirect
from .models import User , Events , submission

# Create your views here.
def homepage(request):
    users = User.objects.filter(hackathon_participants = True) # to filter users using the events only 
    events = Events.objects.all() # to gets all events registered in the database 
    context = {'users': users , 'events': events}
    return render(request  , 'home.html',context)


def user_page(request , pk):
    user = User.objects.get(id = pk)
    context = {'user': user}
    return render(request , 'profile.html', context)

def account_page(request):
    user = request.user
    context = {'user':user }
    return render(request, 'account.html', context )

def events_page(request , pk):
    event = Events.objects.get(id = pk)
    context = {'event':event}
    return render(request, 'events.html', context)

# git init , then git remote add origin and git pull origin master 
# git add .,  git commit -m <message>  then git pull origin master

def registration_confirm(request,pk):
    event = Events.objects.get(id =pk)
    if request.method == 'POST':
        event.participants.add(request.user)
        return redirect('event', pk=event.id)
    
    return render(request , 'event_confirmation.html' , {'event': event})