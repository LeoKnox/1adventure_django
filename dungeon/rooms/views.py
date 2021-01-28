from django.shortcuts import render
from django.http import HttpResponse

from .models import Room, Door

def index(request):
    room_list = Room.objects.all()
    context = {'room_list': room_list}
    return render(request, 'rooms/index.html', context)

def display_room(request, room_id):
    room = Room.objects.get(pk = room_id)
    doors = Door.objects.get(room = room.name)
    context =  { 'room': room, 'door': doors }
    return HttpResponse(request, 'rooms/single_room.html', context)

def edit_room(request, room_id):
    return HttpResponse("Edit this room %s!" % room_id)