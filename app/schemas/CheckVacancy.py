from typing import Annotated

from fastapi import UploadFile, File, Form
from pydantic import BaseModel


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
