from pydantic import BaseModel

class Pet(BaseModel):
    pet_id: int
    name: str
    breed: str
    gender: str
    fleas: int
