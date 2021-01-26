from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    room_list = Room.objects
    doors_list = ', '.join([d.wall for d in room_list])
    return HttpResponse(output)

def display_room(request, room_id):
    return HttpResponse("This is room %s." % room_id)

def edit_room(request, room_id):
    return HttpResponse("Edit this room %s!" % room_id)