from django.shortcuts import render
from .models import Message

def index(request):
    messages = Message.objects.order_by('-timestamp')[:50]
    return render(request, 'chat/index.html', {'messages': messages})
