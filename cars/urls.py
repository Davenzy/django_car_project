from django.urls import path, include, re_path
from . import views
from.views import CarViewSet, CommentViewSet
from rest_framework_nested import routers

app_name = 'cars'

cars_router = routers.SimpleRouter()
cars_router.register(r'cars', CarViewSet)

comments_router = routers.NestedSimpleRouter(cars_router, r'cars', lookup='car')
comments_router.register(r'comments', CommentViewSet, basename='comments')


urlpatterns = [
    path('', views.car_list, name='car_list'),  # Главная страница со списком автомобилей
    path('<int:car_id>/', views.car_detail, name='car_detail'),  # Подробная информация о машине
    path('create/', views.car_create, name='car_create'),  # Создание новой машины
    path('<int:car_id>/edit/', views.car_edit, name='car_edit'),  # Редактирование машины
    path('<int:car_id>/delete/', views.car_delete, name='car_delete'),  # Удаление машины
    path('<int:car_id>/comments/add/', views.add_comment, name='add_comment'),  # Добавление комментария
    path('api/', include(cars_router.urls)),    # работа с api/cars
    path('api/', include(comments_router.urls)),    # работа с api/cars/<car_id>/comments
    path('api/', include('djoser.urls')),   # работа с api/users/
    re_path(r'^api/', include('djoser.urls.authtoken')) # работа с api
]