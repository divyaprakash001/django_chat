from django.shortcuts import redirect, render
from .models import Room,Message

# Create your views here.
def createRoom(request):
  if request.method == 'POST':
    username = request.POST.get('username',None)
    room = request.POST.get('room',None)
    try:
      get_room = Room.objects.get(room_name=room)
      print(get_room)
      if get_room:
        return redirect('room',room_name=room,username=username)
    except Room.DoesNotExist:
      created_room = Room(room_name=room)
      created_room.save()
      return redirect('room',room_name=room,username=username)
    
  return render(request,"index.html")

def messageView(request,room_name,username):
  try:
    get_room = Room.objects.get(room_name=room_name)
    get_messages = Message.objects.filter(room=get_room)
    print(get_room)
    print(get_messages)
    context = {
      "messages":get_messages,
      "user":username,
      "room_name":get_room.room_name,
    }
  except Room.DoesNotExist:
    return redirect('create-room')
  return render(request,'_message.html',context)