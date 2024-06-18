# Dog Breed API

Это Django REST API для управления сущностями собака и порода. Он позволяет пользователям создавать, 
читать, обновлять и удалять записи о собаках и породах через конечные точки RESTful.

Скриншоты работы всех методов в папке /screen

## Установка

1. Клонируйте репозиторий:
   ```sh
   git clone https://github.com/PavelShaura/Dogs_API_DRF.git
   cd Dogs_API_DRF

2. Создайте виртуальное окружение и активируйте его:

`python -m venv venv`
`source venv/bin/activate`

3. Установите зависимости:

`pip install poetry` `poetry install`

4. Создайте файл .env в корневой директории проекта на примере файла .env_example

## Запуск

1.Запустите Docker Compose:

`docker-compose up -d`

2. Примените миграцию базы данных:

`python manage.py migrate`

3. Создайте суперпользователя (необязательно, но необходимо для доступа к интерфейсу администратора):

`python manage.py createsuperuser`

## Использование

1. Запустите сервер:
`python manage.py runserver`  

Конечные точки API будут доступны по адрессу http://localhost:8000/api/

Ендпоинты:

<img width="941" alt="swagger" src="https://github.com/PavelShaura/Dogs_API_DRF/blob/main/screen/SWAGGER.png">

* GET /api/dogs/: Список всех собак 
* POST /api/dogs/: Создать новую собаку 
* GET /api/dogs/<id>/: Получение конкретной собаки
* PUT /api/dogs/<id>/: Обновление конкретной собаки
* DELETE /api/dogs/<id>/: Удалить конкретную собаку
* GET /api/breeds/: Список всех пород
* POST /api/breeds/: Создать новую породу
* GET /api/breeds/<id>/: Получение конкретной породы
* PUT /api/breeds/<id>/: Обновление конкретной породы
* DELETE /api/breeds/<id>/: Удалить определенную породу

