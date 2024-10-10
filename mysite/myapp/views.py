from django.shortcuts import render
from .models import Chatroom,ChatMessage
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
    chatrooms= Chatroom.objects.all()
    context={'chatrooms':chatrooms}
    return render(request,'myapp/index.html',context)

@login_required
def chatroom(request,slug):
    chatroom=Chatroom.objects.get(slug=slug)
    messages=ChatMessage.objects.all().filter(room=chatroom)
    context={'chatroom':chatroom,'messages':messages}
    return render(request,'myapp/room.html',context)


def home(request):
    return render(request,'myapp/intro.html')