from django.shortcuts import render, get_object_or_404, redirect
from django.http.response import HttpResponse
from .models import PersonOptions, CityOptions, SubCategoryOptions, AdditionalOptions
from .forms import OptionsForm, NewTask
from django.utils import timezone
from collections import defaultdict

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
    form = OptionsForm()
    return render(request, 'craigs/index.html', {'form': form})


def settings(request, job_name_id):
    return HttpResponse('<html>'+str(job_name_id)+'</html>')


def create_task(request):
    cities = CityOptions.objects.all()
    subcategories = SubCategoryOptions.objects.values()
    options = AdditionalOptions.objects.values()
    o = defaultdict(list)
    for option in options:
        for k, v in option.items():
            if {option['option_for_frontend']: option['option']} not in o[option['subcategory']]:
                o[option['subcategory']].append({option['option_for_frontend']: option['option']})
    additional_options = dict(o)
    print (additional_options)
    d = defaultdict(list)
    for s in subcategories:
        for k, v in s.items():
            if {s['subcategory_for_frontend']: s['subcategory']} not in d[s['category']]:
                d[s['category']].append({s['subcategory_for_frontend']: s['subcategory']})
    categories = dict(d)
    # print('================')
    # print(categories)
    # print('================')
    # extra_questions = get_questions(request)
    if request.method == "POST":
        form = NewTask(request.POST)
        if form.is_valid():
            # for (question, answer) in form.extra_answers():
            #     print(question, answer)
            print('================')
            print(form.cleaned_data)
        # task = form.save(commit=False)
        # task.user = request.user
        # task.time_update = timezone.now()
        # task.save()
        return redirect('/')

    else:
        form = OptionsForm()
    print('================')
    return render(request, 'craigs/task_edit.html', {
        'form': form,
        'cities': cities,
        'categories': categories,
        'additional_options': additional_options
    })
