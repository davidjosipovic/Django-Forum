from django.urls import path,include
from . import views
from main.views import *


urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('forums', ForumList.as_view()),
    path('threads', ThreadList.as_view()),
    path('posts', PostList.as_view()),
    path('users', UserList.as_view()),
    path('subscriptions', SubscriptionList.as_view()),
    
    
]