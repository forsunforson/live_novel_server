from typing import List, Union
from pydantic import BaseModel

class Message(BaseModel):
    role: str
    content: str

class BaseRequest(BaseModel):
    game: str
    uid: str
    branch: str
    language: str = 'English'

class BaseResponse(BaseModel):
    status_code: int
    result: str

class PlayRequest(BaseRequest):
    content: str

class PlayContext(BaseRequest):
    messages: List[Message]