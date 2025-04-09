from model.abb import ABB
from model.pet import Pet

abb = ABB()

def insert_pet(pet: Pet):
    abb.insert(pet)

def get_all_pets():
    return abb.get_all()

def get_pet_by_id(pet_id: int):
    return abb.search(pet_id)

def delete_pet(pet_id: int):
    return abb.delete(pet_id)
