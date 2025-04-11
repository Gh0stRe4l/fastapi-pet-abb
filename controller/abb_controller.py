from fastapi import APIRouter
from model.pet import Pet
from service.abb_service import ABBService

router = APIRouter(prefix="/abb", tags=["ABB"])

@router.post("/pets")
def create_pet(pet: Pet):
    result = ABBService.create_pet(pet)
    return {"message": "Pet created"} if result else {"error": "Pet ID already exists"}

@router.get("/pets")
def list_pets():
    return ABBService.list_pets()

@router.get("/pets/{pet_id}")
def get_pet(pet_id: int):
    pet = ABBService.get_pet(pet_id)
    return pet if pet else {"error": "Pet not found"}

@router.put("/pets")
def update_pet(pet: Pet):
    updated = ABBService.update_pet(pet)
    return {"message": "Updated"} if updated else {"error": "Pet not found"}

@router.delete("/pets/{pet_id}")
def delete_pet(pet_id: int):
    deleted = ABBService.delete_pet(pet_id)
    return {"message": "Deleted"} if deleted else {"error": "Pet not found"}

@router.get("/pets/traversal/inorder")
def inorder():
    return ABBService.inorder()

@router.get("/pets/traversal/preorder")
def preorder():
    return ABBService.preorder()

@router.get("/pets/traversal/postorder")
def postorder():
    return ABBService.postorder()

@router.get("/pets/exists/{pet_id}")
def check_id_exists(pet_id: int):
    return {"exists": ABBService.id_exists(pet_id)}

@router.get("/pets/count/breed/{breed}")
def count_breed(breed: str):
    return {"count": ABBService.count_by_breed(breed)}

@router.get("/pets/stats/fleas")
def average_fleas(gender: str):
    avg = ABBService.get_average_fleas_by_gender(gender)
    return {"average_fleas": avg}
