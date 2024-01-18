# Web-приложение для определения заполненных форм

## Описание проекта

Приложения для поиска формы в БД

## Технологии

- Linux
- Python
- Poetry
- Django
- DRF
- PostgreSQL
- Docker
- Docker Compose

## Зависимости

Зависимости, необходимые для работы проекта, указаны в файле pyproject.toml.

## Документация

Документация находится по ссылкам:
1. Для загрузки schema.yaml `api/schema/`
2. Swagger `api/schema/swagger-ui`
3. Redoc `api/schema/redoc/`

## Как запустить проект

Для запуска проекта необходимо выполнить следующие шаги:
1. При необходимости установите Docker и Docker Compose на компьютер с помощью инструкции https://docs.docker.com/engine/install/
2. Cклонируйте репозиторий себе на компьютер
3. Создайте файл .env и заполните его, используя образец из файла .env.example
4. Соберите образ с помощью команды `docker-compose build`
5. Запустите контейнеры с помощью команды `docker-compose up`

## Файл .env.example

1. `POSTGRES_DB, POSTGRES_USER, POSTGRES_PASSWORD, DATABASES_HOST` - данные для подключения к БД
2. `SECRET_KEY, DEBUG, ALLOWED_HOSTS`

## Авторы

UlianaSem

## Связь с авторами

https://github.com/UlianaSem/
