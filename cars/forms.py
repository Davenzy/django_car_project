from django import forms
from .models import Car, Comment

class CarForm(forms.ModelForm):
    make = forms.CharField(widget=forms.TextInput(attrs={
        'class' : 'form-control', 'placeholder' : 'Введите марку авто'}))
    model = forms.CharField(widget=forms.TextInput(attrs={
        'class' : 'form-control', 'placeholder' : 'Введите модель авто'}))
    year = forms.CharField(widget=forms.NumberInput(attrs={
        'class' : 'form-control', 'placeholder' : 'Введите год выпука авто'}))
    description = forms.CharField(widget=forms.TextInput(attrs={
        'class' : 'form-control', 'placeholder' : 'Введите описание авто'}))
    class Meta:
        model = Car
        fields = ['make', 'model', 'year', 'description']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']