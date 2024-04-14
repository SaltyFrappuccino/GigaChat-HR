import json
from typing import Union

import requests
from fastapi import APIRouter
from pydantic import BaseModel, Field

from utils.token import get_token

chat_router = APIRouter(prefix="/chat")


class Message(BaseModel):
    content: Union[str, None] = Field(default=None, examples=["Привет!"])


messages = []


@chat_router.post("/")
async def chat(message: Message):
    '''
    Простой запрос к Гигачату
    '''
    message = {'role': 'user', 'content': message.content}
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
    role = response.json()['choices'][0]['message']['role']
    content = response.json()['choices'][0]['message']['content']
    message = {'role': role, 'content': content}
    messages.append(message)
    return response.json()['choices'][0]['message']['content']

@chat_router.get("/")
async def get_messages():
    return messages
