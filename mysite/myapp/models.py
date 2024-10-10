from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Chatroom(models.Model):
    name=models.CharField(max_length=100)
    slug=models.SlugField(unique=True)

class ChatMessage(models.Model):
    user= models.ForeignKey(User,on_delete=models.CASCADE)
    room=models.ForeignKey(Chatroom,on_delete=models.CASCADE)
    message_content=models.TextField()
    date=models.DateField(auto_now=True)

    class Meta:
        ordering=('date',)


