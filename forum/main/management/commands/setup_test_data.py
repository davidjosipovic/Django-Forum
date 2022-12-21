import random

from django.core.management.base import BaseCommand
from django.utils import timezone
from django.db import transaction

from main.models import Forum, Thread, Post, User, Subscription
from main.factory import ForumFactory, ThreadFactory, PostFactory, UserFactory, SubscriptionFactory



num_forums = 10
num_threads = 6
num_posts = 20
num_users = 10

class Command(BaseCommand):
    help = 'Populates the database with dummy data'

    
    @transaction.atomic
    def handle(self, *args, **kwargs):
        self.stdout.write("Deleting old data...")
        models = [Forum, Thread,Post,User, Subscription]
        for m in models:
            m.objects.all().delete()

        self.stdout.write("Creating new data...")

        # Create users
        for i in range(num_users):
            user=UserFactory()

        # Create forums
        for i in range(num_forums):
            forum = ForumFactory()

        # Create threads for each forum
        for j in range(num_threads):
            thread = ThreadFactory()

        # Create posts for each thread
        for k in range(num_posts):
            post=PostFactory()


        self.stdout.write(self.style.SUCCESS('Successfully populated database with dummy data'))

    