from django.shortcuts import render, HttpResponseRedirect
from users.forms import UserLoginForm, UserRegistrationForm, UserProfileForm
from django.contrib import auth, messages
from django.urls import reverse


# Вход
def login(request):
    title = 'Вход'
    if request.method == "POST":            # проверяем получили ли данные для входа пользователя
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('cars:car_list'))
    else:
        form = UserLoginForm()
    
    context = {
        'form' : form,
        'title' : title
    }

    return render(request, 'users/login.html', context)

# Регистрация
def registration(request):
    title = 'Регистрация'
    if request.method == "POST":            # проверяем получили ли данные для регистрации пользователя
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Вы успешно зарегестрировались!')
            return HttpResponseRedirect(reverse('users:login'))
    else:
        form = UserRegistrationForm()

    context = {
        'form' : form,
        'title' : title
    }

    return render(request, 'users/registration.html', context)

# Профиль
def profile(request):
    title = 'Личный кабинет'
    if request.method == "POST":            # если получаем заполненую форму от пользователя то меняем данные
        form = UserProfileForm(instance=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:profile'))
    else:
        form = UserProfileForm(instance=request.user)
    
    context = {
        'form' : form,
        'title' : title
    }
    
    return render(request, 'users/profile.html', context)

# Выход
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('users:login'))     # Перенаправляем на страницу входа