## Установка
1. Склонируйте репозиторий проекта:

   git clone https://github.com/Davenzy/django_car_project.git

2. Перейдите в директорию проекта:

   cd django_car_project

3. Создайте виртуальную среду и активируйте её:

   python -m venv venv
   source venv/bin/activate  # Для Linux/Mac
   venv\Scripts\activate     # Для Windows

4. Установите зависимости:

   pip install -r requirements.txt

## Запуск сервера разработки
1. Выполните миграцию базы данных:

   python manage.py makemigrations
   python manage.py migrate

1. Запустите сервер разработки:

   python manage.py runserver

2. Откройте ваш браузер и перейдите по адресу http://127.0.0.1:8000/, чтобы увидеть приложение в действии.

### если запускаете проект в 

## Документация к API
Ваше приложение предоставляет несколько API-эндпоинтов. Основные из них:

### Получение списка автомобилей
- URL: /api/cars/
- Метод: GET
- Описание: Возвращает список всех автомобилей.
- Ответ:

  [
      {
          "id": 1,
          "brand": "Toyota",
          "model": "Camry",
          "year": 2020,
          ...
      },
      ...
  ]

### Получение информации о конкретном автомобиле
- URL: /api/cars/{id}/
- Метод: GET
- Описание: Возвращает информацию о конкретном автомобиле по ID.
- Пример запроса: /api/cars/1/
- Ответ:

  {
      "id": 1,
      "brand": "Toyota",
      "model": "Camry",
      "year": 2020,
      ...
  }

### Создание нового автомобиля
- URL: /api/cars/
- Метод: POST
- Описание: Создаёт новый автомобиль.
- Тело запроса:

  {
      "brand": "Honda",
      "model": "Civic",
      "year": 2022,
      ...
  }

- Ответ:

  {
      "id": 2,
      "brand": "Honda",
      "model": "Civic",
      "year": 2022,
      ...
  }

## Заключение
Теперь ваше Django-приложение готово к запуску и использованию. Если у вас возникнут во
