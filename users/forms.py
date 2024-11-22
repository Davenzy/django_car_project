from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm

from users.models import User

# форма для входа пользователя
class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={                                   # поле username
        'class' : 'form-control', 'placeholder' : 'Введите имя пользователя'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={                               # поле password
        'class' : 'form-control', 'placeholder' : 'Введите пароль...'}))
    class Meta:
        model = User
        fields = ('username', 'password')                                                       # выводим только поля указанные в кортеже ('username', 'password')

# форма для регистрации пользователя
class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={                                 # поле first_name
        'class' : 'form-control', 'placeholder' : 'Введите ваше имя'}))
    username = forms.CharField(widget=forms.TextInput(attrs={                                   # поле username
        'class' : 'form-control', 'placeholder' : 'Введите имя пользователя'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={                              # поле password1
        'class' : 'form-control', 'placeholder' : 'Введите пароль...'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={                              # поле password2 (для подтверждения пароля)
        'class' : 'form-control', 'placeholder' : 'Повторите пароль...'}))
    class Meta:
        model = User
        fields = ('first_name', 'username', 'password1', 'password2')                           # выводим только поля указанные в кортеже ('first_name', 'username', 'password1', 'password2')

# форма профиля пользователя
class UserProfileForm(UserChangeForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={                                 # поле first_name
        'class' : 'form-control'}))
    username = forms.CharField(widget=forms.TextInput(attrs={                                   # поле username
        'class' : 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={                               # поле password
        'class' : 'form-control'}))
    class Meta:
        model = User
        fields = ('first_name', 'username', 'password')                                         # выводим только поля указанные в кортеже ('first_name', 'username', 'password')