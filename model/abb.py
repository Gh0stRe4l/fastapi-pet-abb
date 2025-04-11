from model.pet import Pet

class Node:
    def __init__(self, pet: Pet):
        self.pet = pet
        self.left = None
        self.right = None

class ABB:
    def __init__(self):
        self.root = None

    def insert(self, root, pet: Pet):
        if root is None:
            return Node(pet)
        if pet.pet_id < root.pet.pet_id:
            root.left = self.insert(root.left, pet)
        elif pet.pet_id > root.pet.pet_id:
            root.right = self.insert(root.right, pet)
        return root

    def search(self, root, pet_id):
        if root is None or root.pet.pet_id == pet_id:
            return root
        if pet_id < root.pet.pet_id:
            return self.search(root.left, pet_id)
        return self.search(root.right, pet_id)

    def update(self, root, pet: Pet):
        node = self.search(root, pet.pet_id)
        if node:
            node.pet = pet
        return node

    def delete(self, root, pet_id):
        if root is None:
            return root
        if pet_id < root.pet.pet_id:
            root.left = self.delete(root.left, pet_id)
        elif pet_id > root.pet.pet_id:
            root.right = self.delete(root.right, pet_id)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            temp = self._min_value_node(root.right)
            root.pet = temp.pet
            root.right = self.delete(root.right, temp.pet.pet_id)
        return root

    @staticmethod
    def _min_value_node(node):
        current = node
        while current.left:
            current = current.left
        return current

    def inorder(self, root, result):
        if root:
            self.inorder(root.left, result)
            result.append(root.pet)
            self.inorder(root.right, result)

    def preorder(self, root, result):
        if root:
            result.append(root.pet)
            self.preorder(root.left, result)
            self.preorder(root.right, result)

    def postorder(self, root, result):
        if root:
            self.postorder(root.left, result)
            self.postorder(root.right, result)
            result.append(root.pet)

    def id_exists(self, root, pet_id):
        return self.search(root, pet_id) is not None

    def count_by_breed(self, root, breed):
        if root is None:
            return 0
        count = 1 if root.pet.breed == breed else 0
        count += self.count_by_breed(root.left, breed)
        count += self.count_by_breed(root.right, breed)
        return count

    def get_average_fleas_by_gender(self, root, gender):
        count, total = self._average_fleas_by_gender(root, gender.lower())
        return total / count if count > 0 else 0

    def _average_fleas_by_gender(self, root, gender_target):
        if root is None:
            return 0, 0
        count = 0
        total = 0
        if root.pet.gender.lower() == gender_target:
            count = 1
            total = root.pet.fleas
        left_count, left_total = self._average_fleas_by_gender(root.left, gender_target)
        right_count, right_total = self._average_fleas_by_gender(root.right, gender_target)
        return count + left_count + right_count, total + left_total + right_total
