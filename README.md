# GigaChat HR API

## Запуск

### Инструкция по запуску проекта через Docker

Из корневой папки проекта:
```shell
docker build -t [your_image_name] .
```
А затем:
```shell
docker run -d -p 8000:8000 [your_image_name]
```

После запуска контейнера вы сможете взаимодействовать с API, используя HTTP-запросы.

### Запуск проекта через Python
Установить зависимости:
```shell
pip install -r requirements.txt
```

И запустить с:
```shell
uvicorn app.main:app --host 127.0.0.1 --port 8000
```

## Swagger UI 

UI интерфейс API доступен по пути `/docs`

## Запросы

### POST - /vacancy/
На вход принимает x-www-form-urlencoded с полем content, которое является запросом на создание вакансии, в респонс возвращает ответ от Гигачата

### POST - /vacancy/check
На вход принимает form-data с полем file, который является pdf-файлом, и полем position - позиция вакансии, в респонс возвращает ответ от Гигачата

### POST - /vacancy/contact
На вход принимает form-data с полем file, который является pdf-файлом, в респонс возвращает контакт, который нашёл Гигачат в формате [название контактной информации]: контактные данные

### POST - /chat/
Отправить сообщение боту

### GET - /chat/
Получить историю общения с ботом