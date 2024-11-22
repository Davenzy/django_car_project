from rest_framework import serializers
from .models import Car, Comment
from users.models import User



class CarSerializer(serializers.ModelSerializer):
    # сделаем поле owner_id только для чтения, что бы нельзя было его изменить
    #owner_id = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Car
        fields = ['id', 'make', 'model', 'year', 'description', 'owner_id']
        read_only_fields = ['owner_id']


    
    def update(self, instance, validated_data):
        # Проверяем, что текущий аутентифицированный пользователь является владельцем или admin
        request = self.context.get('request')
        if not request.user.is_staff and request.user != instance.owner_id:
            raise serializers.ValidationError("Вы не имеете прав на обновление этого объекта.")

        # Обновляем поля
        for attr, value in validated_data.items():
            if attr != 'related':
                setattr(instance, attr, value)

        instance.save()
        return instance
    
    def create(self, validated_data):
        request = self.context.get('request')
        validated_data['owner_id'] = request.user  # Устанавливаем текущего пользователя как владельца
        instance = Car.objects.create(**validated_data)    # Создаем новый объект
        return instance
    

class CommentSerializer(serializers.ModelSerializer):
    # сделаем поле owner_id только для чтения, что бы нельзя было его изменить
    #car_id = serializers.HiddenField()
    #user = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Comment
        fields = ['content', 'user', 'car_id']
        read_only_fields = ['user', 'car_id']  # Указываем, что это поля только для чтения
    
    def create(self, validated_data):
        request = self.context.get('request')
        car_id = self.context['view'].kwargs['car_pk']
        car = Car.objects.get(pk=car_id)
        validated_data['car_id'] = car
        validated_data['user'] = request.user  # Устанавливаем текущего пользователя как владельца
        instance = Comment.objects.create(**validated_data)    # Создаем новый объект
        return instance