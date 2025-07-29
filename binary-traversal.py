import copy
import random


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self):
        left = f"Left: {self.left.value}" if self.left else "Left: None"
        right = f"Right: {self.right.value}" if self.right else "Right: None"
        return f"TreeNode(Value: {self.value}, {left}, {right})"


def insert_into_tree(root, value):
    if root is None:
        return TreeNode(value)
    if value < root.value:
        root.left = insert_into_tree(root.left, value)
    else:
        root.right = insert_into_tree(root.right, value)
    return root


def generate_random_tree(n):
    values = list(range(1, n + 1))
    random.shuffle(values)
    root = None
    for value in values:
        root = insert_into_tree(root, value)
    return root


def pre_order_traversal(root):
    if root is None:
        return []
    return [root.value] + pre_order_traversal(root.left) + pre_order_traversal(root.right)


def collect_tree_levels(root, level=0, levels=None):
    if levels is None:
        levels = []
    if len(levels) <= level:
        levels.append([])
    if root is None:
        levels[level].append(" ")
        return levels
    levels[level].append(str(root.value))
    collect_tree_levels(root.left, level + 1, levels)
    collect_tree_levels(root.right, level + 1, levels)
    return levels


def display_tree(root):
    levels = collect_tree_levels(root)
    max_width = 2 ** (len(levels) - 1)
    result = ""
    for i, level in enumerate(levels):
        spacing = " " * (max_width // (2 ** (i + 1)))
        result += spacing + spacing.join(level) + "\n"
    return result


tree = generate_random_tree(10)
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


def compare_trees(tree1, tree2):
    if tree1 is None and tree2 is None:
        return True
    if tree1 is None or tree2 is None:
        return False
    if tree1.value != tree2.value:
        return False
    return compare_trees(tree1.left, tree2.left) and compare_trees(tree1.right, tree2.right)


if __name__ == "__main__":
    tree = generate_random_tree(10)

    # Сохраняем копию дерева перед обходом
    original_tree = copy.deepcopy(tree)

    # print("Дерево до обхода:")
    # print(display_tree(tree))

    # Классический обход (Pre-order)
    classic_path = pre_order_traversal(tree)

    # Ваш пользовательский обход
    path = []
    traverse_tree(tree)

    # print("Дерево после обхода:")
    # print(display_tree(tree))

    # Проверяем, что структура дерева вернулась в изначальное состояние
    is_same_structure = compare_trees(tree, original_tree)
    print("Структура дерева вернулась в изначальное состояние?", is_same_structure)

    # Проверяем, что результаты обходов совпадают
    is_same_path = classic_path == path
    print("Результаты обходов совпадают?", is_same_path)
