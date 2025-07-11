from django.shortcuts import render, redirect, get_object_or_404
from .models import Project, Task

def index(request):
    projects = Project.objects.all()
    return render(request, 'dashboard/index.html', {'projects': projects})

def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    tasks = project.task_set.all()

    if request.method == 'POST':
        title = request.POST.get('title')
        if title:
            Task.objects.create(project=project, title=title)
        return redirect('project_detail', pk=project.pk)

    return render(request, 'dashboard/project_detail.html', {'project': project, 'tasks': tasks})
