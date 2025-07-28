import random

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self):
        return f"TreeNode({self.value})"



def insert_into_tree(root, value):
    if root is None:
        return TreeNode(value)
    if value < root.value:
        root.left = insert_into_tree(root.left, value)
    else:
        root.right = insert_into_tree(root.right, value)
    return root


def generate_random_tree(n):
    # Шаг 1: Создать последовательный ряд
    values = list(range(1, n + 1))
    # Шаг 2: Перемешать значения
    random.shuffle(values)
    # Шаг 3: Построить дерево

    values = [5, 3, 2, 1, 4, 8, 6, 7, 10, 9]
    root = None
    for value in values:
        root = insert_into_tree(root, value)
    return root


# Методы обхода дерева
def pre_order_traversal(root):
    """Прямой обход (Pre-order): Узел -> Левое поддерево -> Правое поддерево"""
    if root is None:
        return []
    return [root.value] + pre_order_traversal(root.left) + pre_order_traversal(root.right)


def print_tree(root, level=0, prefix="Root: "):
    if root is not None:
        print(" " * (level * 4) + prefix + str(root.value))
        print_tree(root.left, level + 1, "L--- ")
        print_tree(root.right, level + 1, "R--- ")


# Пример использования
tree = generate_random_tree(10)

# Вывод результатов обхода
print(print_tree(tree))
print("Прямой обход (Pre-order):", pre_order_traversal(tree))

path = []


def process_node(node):
    path.append(node.value)


def traverse_tree(root):
    def get_terminator(root):
        while root and (root.left or root.right):
            root = root.right if root.right else root.left
        return root

    marker = TreeNode("Marker")

    while root:
        process_node(root)
        if root.left is marker:  # Второе посещение терминатора
            root = root.right  # Сначала делаем правое поддерево новым root
            root.left = None  # Разрываем служебную ссылку (маркер)
            root.right = None  # Разрываем ссылку на правое поддерево
        elif root.left and root.right:
            terminator = get_terminator(root.left)
            terminator.left = marker  # Устанавливаем маркер
            terminator.right = root.right  # Сохраняем ссылку на правое поддерево
            root = root.left
        else:
            root = root.left if root.left else root.right


traverse_tree(tree)
print(path)
