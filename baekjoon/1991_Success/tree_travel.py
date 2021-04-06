class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.left_node = None
        self.right_node = None

    def add_child(self, parent_value, child_node, is_left) -> bool:
        if self.value == parent_value:
            if is_left:
                self.left_node = child_node
            else:
                self.right_node = child_node
            return True
        if self.left_node is not None and self.left_node.add_child(parent_value, child_node, is_left):
            return True
        if self.right_node is not None and self.right_node.add_child(parent_value, child_node, is_left):
            return True
        return False

# Root -> Left -> Right
def preorder_travel(root_node) -> None:
    result = ""
    stack = [root_node]
    while True:
        try:
            node = stack.pop()
        except IndexError:
            break
        result += node.value
        if node.right_node is not None:
            stack.append(node.right_node)
        if node.left_node is not None:
            stack.append(node.left_node)
    print(result)

# Left -> Root -> Right
def inorder_travel(root_node) -> None:
    result = ""
    stack = []
    node = root_node
    while True:
        while True:
            if node is None:
                break
            stack.append(node)
            node = node.left_node
        try:
            node = stack.pop()
        except IndexError:
            break
        result += node.value
        node = node.right_node
    print(result)

# Left -> Right -> Root
def postorder_travel(root_node) -> None:
    result = ""
    stack = []
    node = root_node
    while True:
        while True:
            if node is None:
                break
            stack.append(node)
            node = node.left_node
        try:
            node = stack.pop()
        except IndexError:
            break
        if node.right_node is None:
            result += node.value
            node = None
        else:
            tmp_node = node.right_node
            node.right_node = None
            stack.append(node)
            node = tmp_node
    print(result)

def solution(node) -> None:
    preorder_travel(node)
    inorder_travel(node)
    postorder_travel(node)
    return

# Input 오류는 고려하지 않는다.
if __name__ == '__main__':
    loop_count = int(input())
    input_data = input().split(" ")
    root_node = Node(input_data[0])
    if "." != input_data[1]:
        root_node.left_node = Node(input_data[1])
    if "." != input_data[2]:
        root_node.right_node = Node(input_data[2])
    for _ in range(loop_count-1):
        input_data = input().split(" ")
        parent_value = input_data[0]
        left_value = input_data[1]
        right_value = input_data[2]
        if "." != left_value:
            child_node = Node(left_value)
            root_node.add_child(parent_value, child_node, True)
        if "." != right_value:
            child_node = Node(right_value)
            root_node.add_child(parent_value, child_node, False)
    solution(root_node)
