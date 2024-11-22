from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('login/', views.login, name='login'),                          # Страница входа
    path('logout/', views.logout, name='logout'),                       # Страница выхода
    path('registration/', views.registration, name='registration'),     # Страница регистрации
    path('profile/', views.profile, name='profile'),                     # Страница профиля
]
