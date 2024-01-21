from django.shortcuts import render
from .models import UserProfile
from multiprocessing import context
from re import I
import json

def home(request):
    stories = []
    
    for user in UserProfile.objects.all():
        items = []
        for story in user.story.all():
            items.append({
                "id" : story.id,
                "type" : "",
                "length" : 3,
                "src" : f'/media/{user.photo}',
        })
    stories.append({
        "id" : str(user.uid),
        "photo" : f'/media/{user.photo}',
        "items" : items,
        "name" : user.name,
    })
    context = { 'stories' : json.dumps(stories)}        
    return render(request, 'home.html', context)