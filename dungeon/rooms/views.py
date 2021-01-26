from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("This is the first room")

def display_room(request, room_id):
    return HttpResponse("This is room %s." % room_id)

def edit_room(request, room_id):
    return HttpResponse("Edit this room %s!" % room_id)