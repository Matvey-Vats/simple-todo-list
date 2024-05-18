from django.shortcuts import render, redirect, HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from .models import Task
from .forms import UserRegistrationForm, LoginForm, TaskCreateForm
from django.contrib import auth

# Create your views here.
@login_required
def task_list(request):
    per_page = 3
    tasks = Task.objects.filter(user=request.user)
    paginator = Paginator(tasks, per_page)
    page_number = request.GET.get('page', 1)
    try:
        tasks = paginator.page(page_number)
    except PageNotAnInteger:
        tasks = paginator.page(1)
    except EmptyPage:
        tasks = paginator.page(paginator.num_pages)
    
    user = request.user
    
    if request.method == "POST":
        form = TaskCreateForm(data=request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            Task.objects.create(user=user, title=title)
            return HttpResponseRedirect(request.META["HTTP_REFERER"])
    else:
        form = TaskCreateForm()
        
    context = {
        'title': "Ваші завдання",
        'tasks': tasks,
        'form': form,
    }
    
    return render(request, 'tasks/task_list.html', context)


def task_remove(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return HttpResponseRedirect(request.META["HTTP_REFERER"])
    


def login(request):
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = auth.authenticate(request, username=username, password=password)
            if user:
                auth.login(request, user)
                return redirect("home")
    else:
        form = LoginForm()
    
    context = {
        'title': 'Авторизація',
        'form': form,
    }
    return render(request, "users/login.html", context)

def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserRegistrationForm()
    
    context = {
        'title': 'Реєстрація',
        'form': form,
    }
    return render(request, "users/register.html", context)


def logout(request):
    auth.logout(request)
    return redirect('login')