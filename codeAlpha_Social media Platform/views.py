from django.shortcuts import render, redirect
from .models import Post

def index(request):
    if request.method == 'POST':
        content = request.POST.get('content')
        if content:
            Post.objects.create(content=content)
        return redirect('/')
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'posts/index.html', {'posts': posts})
