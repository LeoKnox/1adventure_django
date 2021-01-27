from django.shortcuts import render
from django.http import HttpResponse

from .models import Room

def index(request):
    room_list = Room.objects.all()
    context = {'room_list': room_list}
    return render(request, 'rooms/index.html', context)

def display_room(request, room_id):
    return HttpResponse("This is room %s." % room_id)

def edit_room(request, room_id):
    return HttpResponse("Edit this room %s!" % room_id)