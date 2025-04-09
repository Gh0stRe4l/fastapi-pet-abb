from pydantic import BaseModel

class Pet(BaseModel):
    id: int
    name: str
    type: str
