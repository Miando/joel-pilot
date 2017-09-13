from django.shortcuts import render, get_object_or_404, redirect
from django.http.response import HttpResponse
from .models import PersonOptions
from .forms import OptionsForm
from django.utils import timezone


def home_page(request):
    options = PersonOptions.objects.all()

    return render(request, 'craigs/index.html', {'options': options})


def task_edit(request, pk):
    task = get_object_or_404(PersonOptions, pk=pk)

    if request.method == "POST":
        form = OptionsForm(request.POST, instance=task)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.time_update = timezone.now()
            task.save()
            return redirect('/')

    else:
        form = OptionsForm(instance=task)
    return render(request, 'craigs/task_edit.html', {'form': form})

def post_new(request):
    #options = PersonOptions.objects.all()
    form = OptionsForm()
    return render(request, 'craigs/index.html', {'form': form})


def settings(request, job_name_id):
    return HttpResponse('<html>'+str(job_name_id)+'</html>')


def create_task(request):
    if request.method == "POST":
        form = OptionsForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.time_update = timezone.now()
            task.save()
            return redirect('/')

    else:
        form = OptionsForm()
    return render(request, 'craigs/task_edit.html', {'form': form})