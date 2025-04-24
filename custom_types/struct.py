from typing import List
from pydantic import BaseModel

class Message(BaseModel):
    role: str
    content: str

class PlayRequest(BaseModel):
    game: str
    uid: str
    branch: str
    language: str
    content: str

class PlayContext(BaseModel):
    game: str
    uid: str
    branch: str
    language: str
    messages: List[Message]