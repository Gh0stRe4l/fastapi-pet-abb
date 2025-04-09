class Node:
    def __init__(self, pet_data):
        self.pet = pet_data
        self.left = None
        self.right = None

class ABB:
    def __init__(self):
        self.root = None

    def insert(self, new_pet):
        def _insert(current_node, new_pet_data):
            if current_node is None:
                return Node(new_pet_data)
            if new_pet_data.id < current_node.pet.id:
                current_node.left = _insert(current_node.left, new_pet_data)
            elif new_pet_data.id > current_node.pet.id:
                current_node.right = _insert(current_node.right, new_pet_data)
            return current_node

        self.root = _insert(self.root, new_pet)

    def get_all(self):
        result = []

        def _in_order(node):
            if node:
                _in_order(node.left)
                result.append(node.pet)
                _in_order(node.right)

        _in_order(self.root)
        return result

    def search(self, search_id):
        def _search(node, target_id):
            if node is None:
                return None
            if target_id == node.pet.id:
                return node.pet
            elif target_id < node.pet.id:
                return _search(node.left, target_id)
            else:
                return _search(node.right, target_id)

        return _search(self.root, search_id)

    def delete(self, target_id):
        def _delete(node, id_to_delete):
            if node is None:
                return node, False
            if id_to_delete < node.pet.id:
                left_child, deleted_flag = _delete(node.left, id_to_delete)
                node.left = left_child
                return node, deleted_flag
            elif id_to_delete > node.pet.id:
                right_child, deleted_flag = _delete(node.right, id_to_delete)
                node.right = right_child
                return node, deleted_flag
            else:
                if node.left is None:
                    return node.right, True
                elif node.right is None:
                    return node.left, True
                min_node = self._min_value_node(node.right)
                node.pet = min_node.pet
                node.right, _ = _delete(node.right, min_node.pet.id)
                return node, True

        self.root, final_deleted = _delete(self.root, target_id)
        return final_deleted

    @staticmethod
    def _min_value_node(node):
        current = node
        while current.left is not None:
            current = current.left
        return current
