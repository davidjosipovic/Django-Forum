## factories.py
import factory
from factory.django import DjangoModelFactory

from main.models import *

## Defining a factory
class ForumFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Forum

    name = factory.Faker('word')
    description = factory.Faker('sentence')

class ThreadFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Thread

    forum = factory.Iterator(Forum.objects.all())
    title = factory.Faker('sentence')

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker('user_name')
    email = factory.Faker('email')

class PostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Post

    thread = factory.Iterator(Thread.objects.all())
    user = factory.Iterator(User.objects.all())
    body = factory.Faker('text')
   



class SubscriptionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Subscription

    user = factory.Iterator(User.objects.all())
    forum = factory.Iterator(Forum.objects.all())
