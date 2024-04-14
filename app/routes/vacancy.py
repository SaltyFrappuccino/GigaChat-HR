import json
from typing import Annotated

import requests
from fastapi import APIRouter, Form, UploadFile
from pypdf import PdfReader

from app.schemas.CheckVacancy import CheckVacancy
from app.schemas.CreateVacancy import CreateVacancy
from app.utils.token import get_token

vacancy_router = APIRouter(prefix="/vacancy")
messages = []



@vacancy_router.post("/")
async def create(content: CreateVacancy):
    '''
    На вход принимает json с полем content, которое является запросом на создание вакансии, в респонс возвращает ответ от Гигачата
    '''

    message_assistant = {'role': 'system',
                         'content': 'Введи себя как помощник для HR, который помогает составить грамотную вакансию и проверить существующие вакансии на возможные ошибки. Ты пишешь вакансию в компанию "Сбер"'}
    message = {'role': 'user', 'content': content.content}
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


@vacancy_router.post("/check")
async def check(content: CheckVacancy):
    '''
    На вход принимает form-data с полем file, который является pdf-файлом, и полем position - позиция вакансии, в респонс возвращает ответ от Гигачата
    '''
    reader = PdfReader(content.file.file)
    data = "Проверь резюме на позицию " + content.position + "и укажи, чего не достаёт резюме чтобы стать резюме на позицию Middle\n"
    for i in range(0, reader.get_num_pages()):
        data += reader.get_page(i).extract_text()
    message_assistant = {'role': 'system',
                         'content': ''}
    message = {'role': 'user', 'content': data}
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
