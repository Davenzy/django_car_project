from django.db import models
from users.models import User

class Car(models.Model):
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=20)
    year = models.IntegerField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)    # обновляем поле когда созали объект
    updated_at = models.DateTimeField(auto_now=True)    # обновляем поле каждый раз когда его изменяем
    owner_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.make} by {self.owner_id}"
    

class Comment(models.Model):
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car_id = models.ForeignKey(Car, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} on {self.car_id}"
    
