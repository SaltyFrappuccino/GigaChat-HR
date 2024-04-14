import json
from typing import Union

import requests
from fastapi import APIRouter
from pydantic import BaseModel, Field

from app.utils.token import get_token

vacancy_router = APIRouter(prefix="/vacancy")


class Vacancy(BaseModel):
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


messages = []


@vacancy_router.post("/")
async def create_vacancy(vacancy: Vacancy):
    '''
    На вход принимает json с полем content, которое является запросом на создание вакансии, в ответ возвращает ответ от Гигачата
    '''
    message_assistant = {'role': 'system',
                         'content': 'Введи себя как помощник для HR, который помогает составить грамотную вакансию и проверить существующие вакансии на возможные ошибки. Ты пишешь вакансию в компанию "Сбер"'}
    message = {'role': 'user', 'content': vacancy.content}
    messages.extend([message_assistant, message])

    url = "https://gigachat.devices.sberbank.ru/api/v1/chat/completions"

    payload = json.dumps({
        "model": "GigaChat",
        "messages": messages,
        "max_tokens": 512,
    })
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Authorization': 'Bearer ' + get_token(),
    }

    response = requests.request("POST", url, headers=headers, data=payload, verify=False)
    role = response.json()['choices'][0]['message']['role']
    content = response.json()['choices'][0]['message']['content']
    message = {'role': role, 'content': content}
    messages.append(message)
    return messages
