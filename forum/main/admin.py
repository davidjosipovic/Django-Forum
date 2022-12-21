from django.contrib import admin

from main.models import *

models_list = [Forum, Thread,User, Post, Subscription]

## Register your models here.
admin.site.register(models_list)
