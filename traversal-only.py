class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


path = []


def process_node(node):
    # Обрабатывает узел дерева, добавляя его значение в глобальный список path.
    path.append(node.value)


def traverse_tree(root):
    # Выполняет пользовательский обход дерева с использованием маркеров.
    def get_terminator(root):
        while root and (root.left or root.right):
            root = root.right if root.right else root.left
        return root

    marker = TreeNode("Marker")

    while root:
        process_node(root)
        if root.left is marker:  # Второе посещение терминатора
            root_right = root.right  # Сохраняем корень правого поддерева
            root.left = None  # Разрываем служебную ссылку (маркер)
            root.right = None  # Разрываем ссылку на правое поддерево
            root = root_right  # Переходим к обработке правого поддерева
        elif root.left and root.right:
            terminator = get_terminator(root.left)
            terminator.left = marker  # Устанавливаем маркер
            terminator.right = root.right  # Сохраняем ссылку на правое поддерево
            root = root.left
        else:
            root = root.left if root.left else root.right
