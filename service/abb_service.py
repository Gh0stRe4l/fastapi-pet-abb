from model.abb import ABB
from model.pet import Pet

abb = ABB()

class ABBService:
    @staticmethod
    def create_pet(pet: Pet):
        if abb.id_exists(abb.root, pet.pet_id):
            return None
        abb.root = abb.insert(abb.root, pet)
        return pet

    @staticmethod
    def list_pets():
        result = []
        abb.inorder(abb.root, result)
        return result

    @staticmethod
    def get_pet(pet_id: int):
        node = abb.search(abb.root, pet_id)
        return node.pet if node else None

    @staticmethod
    def update_pet(pet: Pet):
        return abb.update(abb.root, pet)

    @staticmethod
    def delete_pet(pet_id: int):
        pet = ABBService.get_pet(pet_id)
        if pet:
            abb.root = abb.delete(abb.root, pet_id)
        return pet

    @staticmethod
    def inorder():
        result = []
        abb.inorder(abb.root, result)
        return result

    @staticmethod
    def preorder():
        result = []
        abb.preorder(abb.root, result)
        return result

    @staticmethod
    def postorder():
        result = []
        abb.postorder(abb.root, result)
        return result

    @staticmethod
    def id_exists(pet_id: int):
        return abb.id_exists(abb.root, pet_id)

    @staticmethod
    def count_by_breed(breed: str):
        return abb.count_by_breed(abb.root, breed)

    @staticmethod
    def get_average_fleas_by_gender(gender: str):
        return abb.get_average_fleas_by_gender(abb.root, gender)
