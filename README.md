## Установка
1. Склонируйте репозиторий проекта:

   `git clone https://github.com/Davenzy/django_car_project.git`

2. Перейдите в директорию проекта:

   `cd django_car_project`

3. Создайте виртуальную среду и активируйте её:

   ```python -m venv venv
   source venv/bin/activate  # Для Linux/Mac
   venv\Scripts\activate     # Для Windows

4. Установите зависимости:

   `pip install -r requirements.txt`

## Запуск сервера разработки
1. Выполните миграцию базы данных:

   ```python manage.py makemigrations
   python manage.py migrate

1. Запустите сервер разработки:

   `python manage.py runserver`

2. Откройте ваш браузер и перейдите по адресу http://127.0.0.1:8000/, чтобы увидеть приложение в действии.

### если запускаете проект в 

## Документация к API
Ваше приложение предоставляет несколько API-эндпоинтов. Основные из них:

### Регистрация токена пользователя
- URL: /api/token/login/
- Метод: POST
- Описание: Регистрация токена пользователя для аутентификации.
- Тело запроса:

  ```{
      "username": "newusername",
      "password": "strongpassword"
  }

- Ответ:

  ```{
      "auth_token": "your_generated_token"
  }

### Удаление токена пользователя
- URL: /api/token/logout/
- Метод: POST
- Описание: Удаление токена пользователя для аутентификации.
- Тело запроса в headers:

  ```{
      "Authorization": "Token {your_token}"
  }```

- Ответ:

  ```{
      "auth_token": "your_generated_token"
  }

> [!WARNING]
> Предупреждение: Для использования API вам потребуется передавать ваш token в headers в следующем формате: ```{"Authorization": "Token {your_token}"}```

### Получение списка автомобилей
- URL: /api/cars/
- Метод: GET
- Описание: Возвращает список всех автомобилей.
- Ответ:

  ``` [
      {
          "id": 1,
          "make": "Toyota",
          "model": "Camry",
          "year": 2020,
          ...
      },
      ...
  ]

### Получение информации о конкретном автомобиле
- URL: /api/cars/{car_id}/
- Метод: GET
- Описание: Возвращает информацию о конкретном автомобиле по ID.
- Пример запроса: /api/cars/1/
- Ответ:

  ``` {
      "id": 1,
      "make": "Toyota",
      "model": "Camry",
      "year": 2020,
      ...
  }

### Создание нового автомобиля
- URL: /api/cars/
- Метод: POST
- Описание: Создаёт новый автомобиль.
- Тело запроса:

  ``` {
      "make": "Honda",
      "model": "Civic",
      "year": 2022,
      ...
  }

- Ответ:

  ``` {
      "id": 2,
      "make": "Honda",
      "model": "Civic",
      "year": 2022,
      ...
  }

### Обновление информации о автомобиле
- URL: /api/cars/{car_id}/
- Метод: PUT
- Описание: Обновляет информацию о конкретном автомобиле по ID.
- Тело запроса:

  ``` {
      "make": "Honda",
      "model": "Accord",
      "year": 2021,
      ...
  }

- Ответ:

  ``` {
      "id": 2,
      "make": "Honda",
      "model": "Accord",
      "year": 2021,
      ...
  } ```

### Удаление автомобиля
- URL: /api/cars/{car_id}/
- Метод: DELETE
- Описание: Удаляет автомобиль по ID.

### Получение комментариев к автомобилю
- URL: /api/cars/{car_id}/comments/
- Метод: GET
- Описание: Возвращает список комментариев к автомобилю по ID.
- Пример запроса: /api/cars/1/comments/
- Ответ:

  ``` [
      {
          "id": 1,
          "car_id": 1,
          "user": "username",
          "comment": "Отличный автомобиль!",
          ...
      }
  ] ```

### Добавление нового комментария к автомобилю
- URL: /api/cars/{car_id}/comments/
- Метод: POST
- Описание: Создаёт новый комментарий к автомобилю.
- Тело запроса:

  ``` {
      "user": "username",
      "comment": "Этот автомобиль мне очень нравится."
  } ```

- Ответ:

  ``` {
      "id": 2,
      "car_id": 1,
      "user": "username",
      "comment": "Этот автомобиль мне очень нравится."
  } ```

## Заключение
Теперь ваше Django-приложение готово к запуску и использованию. Если у вас возникнут во
