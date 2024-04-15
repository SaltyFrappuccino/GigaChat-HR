import json
from typing import Annotated

import requests
from fastapi import APIRouter, Form, UploadFile, Body
from pypdf import PdfReader

from app.utils.config import debug
from app.utils.token import get_token

vacancy_router = APIRouter(prefix="/vacancy")


@vacancy_router.post("/")
async def create(content: Annotated[str, Body(examples=[
    'Напиши вакансию на Middle Java разработчика, который будет работать с микросервисной архитектурой через Разработку-Тестированием. \nНужны знания JUnit, Java, знания Архитектуры.\nУкажи все базовые Хард и Софт скиллы на подобную вакансию.'])]):
    '''
    На вход принимает x-www-form-urlencoded с полем content, которое является запросом на создание вакансии, в респонс возвращает ответ от Гигачата
    '''
    messages = []
    message_assistant = {'role': 'system',
                         'content': 'Введи себя как Глава HR отдела, который помогает составить грамотную вакансию.'}
    message = {'role': 'user', 'content': content}
    if message_assistant not in messages:
        messages.extend([message_assistant, message])
    else:
        messages.append(message)
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
    if debug == True:
        print(response.json())
    role = response.json()['choices'][0]['message']['role']
    content = response.json()['choices'][0]['message']['content']
    message = {'role': role, 'content': content}
    messages.append(message)
    return messages


@vacancy_router.post("/check")
async def check(file: Annotated[UploadFile, Form()], position: Annotated[str, Form()]):
    '''
    На вход принимает form-data с полем file, который является pdf-файлом, и полем position - позиция вакансии, в респонс возвращает ответ от Гигачата
    '''
    messages = []
    reader = PdfReader(file.file)
    data = ""
    for i in range(0, reader.get_num_pages()):
        data += reader.get_page(i).extract_text()
    message_assistant = {'role': 'system',
                         'content': 'Ты Senior Программист, который проверяет резюме на позицию ' + position + ". Укажи все недостатки резюме, которые ты видишь."}
    message = {'role': 'user', 'content': data}
    if message_assistant not in messages:
        messages.extend([message_assistant, message])
    else:
        messages.append(message)
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
    if debug == True:
        print(response.json())
    role = response.json()['choices'][0]['message']['role']
    content = response.json()['choices'][0]['message']['content']
    message = {'role': role, 'content': content}
    messages.append(message)
    return messages


@vacancy_router.post("/contact")
async def contact(file: Annotated[UploadFile, Form()]):
    messages = []
    '''
    На вход принимает form-data с полем file, который является pdf-файлом, в респонс возвращает контакт, который нашёл Гигачат в формате [название контактной информации]: контактные данные\n
    '''
    reader = PdfReader(file.file)
    data = ""
    for i in range(0, reader.get_num_pages()):
        data += reader.get_page(i).extract_text()
    message_assistant = {'role': 'system',
                         'content': 'Ты автоматическая система для распознавания контактных данных из резюме. Укажи в список все контактные данные, которые присутствуют в резюме. Указывай их в строгом формате [название контактной информации]: [контактные данные], без квадратных скобок.'}
    message = {'role': 'user', 'content': data}
    if message_assistant not in messages:
        messages.extend([message_assistant, message])
    else:
        messages.append(message)
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
    if debug == True:
        print(response.json())
    role = response.json()['choices'][0]['message']['role']
    content = response.json()['choices'][0]['message']['content']
    message = {'role': role, 'content': content}
    messages.append(message)
    return messages
