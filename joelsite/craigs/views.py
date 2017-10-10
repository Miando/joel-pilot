from django.shortcuts import render, get_object_or_404, redirect
from django.http.response import HttpResponse
from .models import PersonOptions, CityOptions, SubCategoryOptions, AdditionalOptions, ScrapedInfo
from .forms import OptionsForm, NewTask, UserForm, IsActiveForm, EditOption
from django.utils import timezone
from collections import defaultdict
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail


def last_items(request, pk):
    if not request.user.is_authenticated():
        return render(request, 'craigs/login.html')
    else:
        try:
            scraped_ids = []
            for options in PersonOptions.objects.filter(user=request.user, pk=pk):
                for scraped in options.scrapedinfo_set.all():
                    scraped_ids.append(scraped.pk)
            last_items = ScrapedInfo.objects.filter(pk__in=scraped_ids)
            print(last_items)

        except PersonOptions.DoesNotExist:
            last_items = []
        return render(request, 'craigs/last_items.html', {'last_items': last_items})


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
                return redirect('create_task')

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


def edit_option(request):
    if not request.user.is_authenticated():
        return render(request, 'craigs/login.html')
    if request.method == "POST":
        form = EditOption(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            p = PersonOptions.objects.get(pk=data['pk'])
            p.is_active = data['is_active']
            p.save()
            # for (question, answer) in form.extra_answers():
            #     print(question, answer)
            print('================')
            print(form.cleaned_data)
            return redirect('/')


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


def task_delete(request, pk):
    print(pk)
    option = PersonOptions.objects.get(pk=pk)
    option.delete()
    return redirect('/')


def create_task(request):
    if not request.user.is_authenticated():
        return render(request, 'craigs/login.html')
    cities = CityOptions.objects.values()
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
    cc = defaultdict(list)
    for c in cities:
        for k, v in c.items():
            if {c['city_for_frontend']: c['city']} not in cc[c['state']]:
                cc[c['state']].append({c['city_for_frontend']: c['city']})
    cities = dict(cc)
    # print('================')
    # print(cities)
    # print('================')
    if request.method == "POST":
        form = NewTask(request.POST)
        if form.is_valid():
            print('================')
            print(form)
            print(form.cleaned_data)
            data = form.cleaned_data
            options = ''
            for k, v in data.items():
                if k[:3] == 'opt' and v != '':
                    options += options + '&' + v
            print (options)
            if data.get('job_name', '') == '':
                form = OptionsForm()
                error_massege = 'Name of task is empty'
                print('================')
                return render(request, 'craigs/task_edit.html', {
                    'form': form,
                    'error_massege': error_massege,
                    'cities': cities,
                    'categories': categories,
                    'additional_options': additional_options
                })
            p = PersonOptions(
                user=request.user,
                options=options,
                is_active=True,#data['is_active'],
                city=data.get('village', ''),
                job_name=data.get('job_name', ''),
                category=data.get('category', ''),
                subcategory=data.get('subcategory', ''),
                keyword=data.get('keyword', ''),
                stop_word=data.get('stop_word', ''),
                url=data.get('url1', ''),
            )
            p.save()
            send_mail(
                'Created new task: {}'.format(data.get('job_name', '')),
                'Task "{}" is active'.format(data.get('job_name', '')),
                'mykhailo.kuznietsov@gmail.com',
                [p.user.email],
                fail_silently=False,
                # html_message=message
            )
            print("--------")
        else:
            form = OptionsForm()
            error_massege = 'Name of task is empty'
            print('================')
            return render(request, 'craigs/task_edit.html', {
                'form': form,
                'error_massege': error_massege,
                'cities': cities,
                'categories': categories,
                'additional_options': additional_options
            })

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
