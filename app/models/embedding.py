from pydantic import BaseModel


class Embedding(BaseModel):
    text: str
    embedding: list
