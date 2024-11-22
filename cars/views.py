from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from cars.permissions import IsOwnerOrReadOnly
from .models import Car, Comment
from .forms import CarForm, CommentForm
from django.urls import reverse
from users.models import User
from .serializers import CarSerializer, CommentSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import GenericViewSet
from rest_framework.views import APIView
from rest_framework import mixins
from rest_framework.response import Response
from rest_framework import status


# Главная страница со списком автомобилей
def car_list(request):
    title = 'Список машин'
    cars = Car.objects.all()        # получаем список автомобилей из БД и передаем их в context

    context = {
        'cars': cars,
        'title' : title
    }

    return render(request, 'cars/car_list.html', context)

# Страница для отображения деталей автомобиля
def car_detail(request, car_id):
    car = get_object_or_404(Car, id=car_id)                             # получаем объект car из бд, где car_id совпадает с car_id из url
    comments = Comment.objects.filter(car_id=car_id)                    # получаем все коментарии из бд, отномящиеся к выбранной машине (car_id=car_id)
    title = f'{car.make} {car.model} Владелец: {car.owner_id} - Детали'    # формируем title для информации на сайте
    
    context = {
        "car" : car,
        'comments': comments,
        'title' : title
    }

    return render(request, 'cars/car_detail.html', context)

# Создание новой машины (только для авторизованных пользователей)
@login_required
def car_create(request):
    title = 'Добавить новую машину'
    if request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)                                           # сохраняем форму в бд
            obj.owner_id = User.objects.get(pk=request.user.id)                        # изменяем поле owner на id текущего пользователя
            obj.save()                                                              # перезапишем форму
            return HttpResponseRedirect(reverse('cars:car_detail', args=[obj.id]))  # перенаправим пользователя на страницу с информацией о текущей машине (args=[obj.id])
    else:
        form = CarForm()
    
    context = {
        'form': form,
        'title' : title
    }

    return render(request, 'cars/car_form.html', context)

# Редактирование машины
@login_required
def car_edit(request, car_id):
    title = 'Изменить машину'
    car = get_object_or_404(Car, id=car_id)                             # получаем car из бд где id совпадает с car_id из url (id=car_id)
    if request.method == 'POST':
        form = CarForm(request.POST, instance=car)                      # получаем форму Car для работы с ней
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('cars:car_list'))       # после внесения правок перенаправляем пользователя на главную страницу
    else:
        form = CarForm(instance=car)
    
    context = {
        'form': form,
        'car' : car,
        'title' : title
    }

    return render(request, 'cars/car_form.html', context)

# Удаление машины
@login_required
def car_delete(request, car_id):
    car = get_object_or_404(Car, id=car_id)                             # получаем car из бд где id совпадает с car_id из url (id=car_id)
    car.delete()                                                        # удаляем полученный объект
    return HttpResponseRedirect(reverse('cars:car_list'))

# Добавление комментария к машине
@login_required
def add_comment(request, car_id):
    title = 'Добавить комментарий'
    car = get_object_or_404(Car, id=car_id)                             # получаем car из бд где id совпадает с car_id из url (id=car_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)                                # будем работать с формой комментариев CommentForm
        if form.is_valid():
            comment = form.save(commit=False)                           # сохраним комеентарий в бд
            comment.car_id = car                                           # перезапишем переменную car на полученный car ранее
            comment.user = request.user                                 # перезапишем автора комментария как имя текущего пользователя
            comment.save()                                              # сохраним полученную форму в бд
            return HttpResponseRedirect(reverse('cars:car_detail', args=[car.id]))
    else:
        form = CommentForm(request.POST)

    context = {
        'form': form,
        'title' : title
    }

    return render(request, 'cars/car_comment.html', context)


class CarViewSet(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )


class CommentViewSet(mixins.CreateModelMixin,
                     mixins.ListModelMixin,
                     GenericViewSet):
    serializer_class = CommentSerializer

    def get_queryset(self):
        # Получаем car_id из URL и фильтруем комментарии по автомобилю
        car_id = self.kwargs['car_pk']  # 'car_pk' по умолчанию используется для вложенных роутеров
        return Comment.objects.filter(car_id=car_id)