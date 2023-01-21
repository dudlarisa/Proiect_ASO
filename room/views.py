
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from django.http import HttpResponse, JsonResponse

from .models import Room, Message

@login_required
def rooms(request):
    rooms = Room.objects.all()

    return render(request, 'room/rooms.html', {'rooms': rooms})

@login_required
def room(request, room):
        username = request.user.username
        room_details = Room.objects.get(name=room)
        return render(request, 'room/room.html', {
            'username' : username,
            'room': room,
            'room_details': room_details
        })

@login_required
def checkview(request):
    #if request.user.is_authenticated():
    username = request.user.username
    room = request.POST['room_name']

    if Room.objects.filter(name=room).exists():
        return redirect('/rooms/'+room+'/')
    else:
        new_room = Room.objects.create(name=room)
        new_room.save()
        return redirect('/rooms/'+room+'/')

@login_required
def send(request):
    message = request.POST['message']
    username = request.POST['username']
    room = request.POST['room']

    new_message = Message.objects.create(value=message, user=username, room=room)
    new_message.save()
    return HttpResponse('Message sent successfully!')

@login_required
def getMessages(request, room):
    room_details = Room.objects.get(name=room)
    messages = Message.objects.filter(room=room_details.name)
    print(room_details)
    return JsonResponse({"messages": list(messages.values())})

@login_required
def typing(request):
     message = request.POST['message']
     return JsonResponse({"message": message})