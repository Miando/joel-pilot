from django.shortcuts import render, get_object_or_404, redirect
from django.http.response import HttpResponse
from .models import PersonOptions, CityOptions, SubCategoryOptions, AdditionalOptions
from .forms import OptionsForm, NewTask, UserForm, IsActiveForm
from django.utils import timezone
from collections import defaultdict
from django.contrib.auth import authenticate, login, logout


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                options = PersonOptions.objects.all()
                return render(request, 'craigs/index.html', {'options': options})
            else:
                return render(request, 'craigs/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'craigs/login.html', {'error_message': 'Invalid login'})
    return render(request, 'craigs/login.html')


def register(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('/')

    context = {
        "form": form,
    }
    return render(request, 'craigs/register.html', context)


def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'craigs/login.html', context)


def home_page(request):
    if not request.user.is_authenticated():
        return render(request, 'craigs/login.html')
    if request.method == "POST":
        form = IsActiveForm(request.POST)

        if form.is_valid():

            get_object_or_404(PersonOptions, pk=pk)

            task = form.save(commit=False)
            task.is_active = request.is_active
            task.time_update = timezone.now()
            task.save()
            return redirect('/')
    else:
        form = IsActiveForm()

    options = PersonOptions.objects.filter(user=request.user)
    return render(request, 'craigs/index.html', {'options': options, 'form': form})


def task_edit(request, pk):
    if not request.user.is_authenticated():
        return render(request, 'craigs/login.html')
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


def settings(request, job_name_id):
    return HttpResponse('<html>'+str(job_name_id)+'</html>')


def create_task(request):
    if not request.user.is_authenticated():
        return render(request, 'craigs/login.html')
    cities = CityOptions.objects.order_by('city')
    subcategories = SubCategoryOptions.objects.values()
    options = AdditionalOptions.objects.values()
    o = defaultdict(list)
    for option in options:
        for k, v in option.items():
            if {option['option_for_frontend']: option['option']} not in o[option['subcategory']]:
                o[option['subcategory']].append({option['option_for_frontend']: option['option']})
    additional_options = dict(o)
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
            data = form.cleaned_data
            options = ''
            for k, v in data.items():
                if k[:3] == 'opt' and v != '':
                    options += options + '&' + v
            print (options)

            p = PersonOptions(
                user=request.user,
                options=options,
                is_active=data['is_active'],
                city=data['village'],
                job_name=data['job_name'],
                category=data['category'],
                subcategory=data['subcategory'],
                keyword=data['keyword'],
            )
            p.save()
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
