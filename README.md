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
На вход принимает json с полем content, которое является запросом на создание вакансии, в респонс возвращает ответ от Гигачата

```json
{
  "content": "Напиши вакансию на Junior Java Разработчик. Напиши вакансию на Middle Java разработчика, который будет работать с микросервисной архитектурой через Разработку-Тестированием. \nНужны знания JUnit, Java, знания Архитектуры.\nУкажи все базовые Хард и Софт скиллы на подобную вакансию.",
  "model_config": {
    "json_schema_extra": {
      "response": [
        {
          "role": "user",
          "content": "Напиши вакансию на Junior Java Разработчик. Напиши вакансию на Middle Java разработчика, который будет работать с микросервисной архитектурой через Разработку-Тестированием. \nНужны знания JUnit, Java, знания Архитектуры.\nУкажи все базовые Хард и Софт скиллы на подобную вакансию."
        },
        {
          "role": "assistant",
          "content": "Вакансия на Junior Java Разработчик:\n\nТребования:\n- Знание Java SE 8+\n- Опыт работы с Spring Framework (Core, Boot)\n- Опыт работы с SQL\n- Знание основных паттернов проектирования\n- Умение работать с системами контроля версий (Git)\n- Знание основных принципов ООП\n- Умение работать в команде\n\nЖелательно:\n- Знание JUnit\n- Опыт работы с микросервисной архитектурой\n- Знание Docker\n- Опыт работы с NoSQL базами данных (MongoDB, Elasticsearch)\n- Знание Kubernetes\n\nВакансия на Middle Java разработчика, работающего с микросервисной архитектурой через Разработку-Тестирование:\n\nТребования:\n- Знание Java SE 8+\n- Опыт работы с Spring Framework (Core, Boot)\n- Опыт работы с SQL\n- Знание основных паттернов проектирования\n- Умение работать с системами контроля версий (Git)\n- Знание основных принципов ООП\n- Умение работать в команде\n\nЖелательно:\n- Знание JUnit\n- Опыт работы с микросервисной архитектурой\n- Знание Docker\n- Опыт работы с NoSQL базами данных (MongoDB, Elasticsearch)\n- Знание Kubernetes\n- Опыт работы с CI/CD инструментами (Jenkins, GitLab CI/CD)\n- Опыт работы с системами мониторинга (Prometheus, Grafana)\n- Опыт работы с системами логирования (Log4j, Logback)\n- Опыт работы с системами управления конфигурацией (Ansible, Terraform)\n- Опыт работы с инструментами автоматизации тестирования (Selenium, Cucumber)"
        }
      ]
    }
  }
}
```

### POST - /vacancy/check
На вход принимает form-data с полем file, который является pdf-файлом, и полем position - позиция вакансии, в респонс возвращает ответ от Гигачата

```json
{
  "file": "string",
  "position": "string",
  "model_config": {
    "json_schema_extra": {
      "request": {
        "file": "File here",
        "position": "Junior Java Developer"
      },
      "Content-Type": "multipart/form-data"
    }
  }
}
```

### GET - /chat/
Получить историю общения с ботом


### POST - /chat/
Отправить сообщение боту

Запрос: 

```json 
{
  "content": "Привет!"
}
```

Ответ:
```plain
"Здравствуйте!"
```

## Схемы

### CheckVacancy
```python
class CheckVacancy(BaseModel):
    file: Annotated[UploadFile, Form()]
    position: str
    model_config = {
        "json_schema_extra": {
            "request": {
                "file": 'File here',
                'position': 'Junior Java Developer'
            },
            'Content-Type':'multipart/form-data'
        }
    }
```

### CreateVacancy
```python
class CreateVacancy(BaseModel):
    content: Union[str, None] = Field(default=None, examples=[
        "Напиши вакансию на Junior Java Разработчик. Напиши вакансию на Middle Java разработчика, который будет работать с микросервисной архитектурой через Разработку-Тестированием. \nНужны знания JUnit, Java, знания Архитектуры.\nУкажи все базовые Хард и Софт скиллы на подобную вакансию."])
    model_config = {
        "json_schema_extra": {
            "response": [
                {
                    "role": "user",
                    "content": "Напиши вакансию на Junior Java Разработчик. Напиши вакансию на Middle Java разработчика, который будет работать с микросервисной архитектурой через Разработку-Тестированием. \nНужны знания JUnit, Java, знания Архитектуры.\nУкажи все базовые Хард и Софт скиллы на подобную вакансию."
                },
                {
                    "role": "assistant",
                    "content": "Вакансия на Junior Java Разработчик:\n\nТребования:\n- Знание Java SE 8+\n- Опыт работы с Spring Framework (Core, Boot)\n- Опыт работы с SQL\n- Знание основных паттернов проектирования\n- Умение работать с системами контроля версий (Git)\n- Знание основных принципов ООП\n- Умение работать в команде\n\nЖелательно:\n- Знание JUnit\n- Опыт работы с микросервисной архитектурой\n- Знание Docker\n- Опыт работы с NoSQL базами данных (MongoDB, Elasticsearch)\n- Знание Kubernetes\n\nВакансия на Middle Java разработчика, работающего с микросервисной архитектурой через Разработку-Тестирование:\n\nТребования:\n- Знание Java SE 8+\n- Опыт работы с Spring Framework (Core, Boot)\n- Опыт работы с SQL\n- Знание основных паттернов проектирования\n- Умение работать с системами контроля версий (Git)\n- Знание основных принципов ООП\n- Умение работать в команде\n\nЖелательно:\n- Знание JUnit\n- Опыт работы с микросервисной архитектурой\n- Знание Docker\n- Опыт работы с NoSQL базами данных (MongoDB, Elasticsearch)\n- Знание Kubernetes\n- Опыт работы с CI/CD инструментами (Jenkins, GitLab CI/CD)\n- Опыт работы с системами мониторинга (Prometheus, Grafana)\n- Опыт работы с системами логирования (Log4j, Logback)\n- Опыт работы с системами управления конфигурацией (Ansible, Terraform)\n- Опыт работы с инструментами автоматизации тестирования (Selenium, Cucumber)"
                }
            ]
        }
    }
```
