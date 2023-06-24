from django.shortcuts import render, redirect
from .models import User , Events , Submission
from django.http import HttpResponse
from .forms import SubmissionForm,CustomUserCreateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout


# Create your views here.
def login_page(request):
    page = 'login'
    if request.method == "POST":
        user = authenticate(email = request.POST['email'], password = request.POST['password'])
        if user is not None:
            login(request, user)
            return redirect('home')

    context = {'page':page }
    return render(request ,'login.html' , context )

def logout_page(request):
    logout(request)
    return redirect('login')

def register_page(request): # registration  and login on the same page
    form = CustomUserCreateForm()
    if request.method == 'POST':
        form = CustomUserCreateForm(request.POST)
        if form.is_valid():
            user =form.save(commit = False)
            user.save()
            login(request, user)
            return redirect('home')

    page = 'register'
    context = {'page': page , 'form':form}
    return render(request ,'login.html' , context )

def homepage(request):
    users = User.objects.filter(hackathon_participants = True) # to filter users using the events only 
    events = Events.objects.all() # to gets all events registered in the database 
    context = {'users': users , 'events': events}
    return render(request  , 'home.html',context)


def user_page(request , pk): # for each and every user to have a profile page 
    user = User.objects.get(id = pk)
    context = {'user': user}
    return render(request , 'profile.html', context)

@login_required(login_url= '/login')
def account_page(request): # the account page for each user 
    user = request.user
    context = {'user':user }
    return render(request, 'account.html', context )

def events_page(request , pk): # the event page for all u sers 
    event = Events.objects.get(id = pk)
    registered = request.user.events.filter(id = event.id).exists()
    submitted  = Submission.objects.filter(participants = request.user, event = event).exists()

    context = {'event':event , 'registered': registered , 'submitted': submitted}
    return render(request, 'events.html', context)
 

@login_required(login_url= '/login')
def registration_confirm(request,pk):
    event = Events.objects.get(id =pk)
    if request.method == 'POST':
        event.participants.add(request.user)
        return redirect('event', pk=event.id)
    
    return render(request , 'event_confirmation.html' , {'event': event})


def project_submission(request, pk ): # handling of project submission 
    event = Events.objects.get(id = pk )
    form = SubmissionForm()
    if request.method == 'POST':
        form = SubmissionForm( request.POST, initial={'event': event , 'participants' : request.user})
        if form.is_valid():
            submission = form.save(commit = False)
            submission.participant = request.user
            submission.event = event
            submission.save()
            
            return redirect('account')
    context = {'event' : event , 'form':form}
    return render(request , 'submit_form.html', context)

@login_required(login_url= '/login')
def update_submission(request , pk ): # this line of code is for updating the submission page
    submit   = Submission.objects.get( id = pk )
    if request.user != submit.participants:
        return HttpResponse("You are not allowed here !!!!!")
    event = Submission.event
    form = SubmissionForm(instance = submit)

    if request.method == 'POST':
        form = SubmissionForm(request.POST , instance= submit)
        if form.is_valid():
            form.save()
            return redirect('account')

    context = {'form': form  , 'event': event   }
    return render(request ,'submit_form.html', context)

