from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.generic import ListView
from main.models import Forum, Thread,User, Post, Subscription

class ForumList(ListView):
    model = Forum
class ThreadList(ListView):
    model = Thread
class UserList(ListView):
    model = User
class PostList(ListView):
    model = Post
class SubscriptionList(ListView):
    model = Subscription




def homepage(request):
    return render(request, 'base_generic.html')

