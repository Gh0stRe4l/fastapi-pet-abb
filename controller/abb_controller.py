from fastapi import APIRouter, HTTPException
from model.pet import Pet
from service import abb_service

router = APIRouter()

@router.post("/pets")
def create_pet(pet: Pet):
    abb_service.insert_pet(pet)
    return {"message": "Pet inserted successfully"}

@router.get("/pets")
def get_pets():
    return abb_service.get_all_pets()

@router.get("/pets/{pet_id}")
def get_pet(pet_id: int):
    pet = abb_service.get_pet_by_id(pet_id)
    if pet is None:
        raise HTTPException(status_code=404, detail="Pet not found")
    return pet

@router.delete("/pets/{pet_id}")
def delete_pet(pet_id: int):
    deleted = abb_service.delete_pet(pet_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Pet not found")
    return {"message": "Pet deleted successfully"}
