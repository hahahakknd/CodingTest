class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.left_node = None
        self.right_node = None

    def add_child(self, child_node) -> None:
        if self.value > child_node.value:
            self.left_node = child_node
        else:
            self.right_node = child_node

def find_leaf_node(root_node, value) -> Node:
    leaf_node = root_node
    while True:
        if leaf_node.value > value:
            if leaf_node.left_node is None:
                break
            leaf_node = leaf_node.left_node
        else:
            if leaf_node.right_node is None:
                break
            leaf_node = leaf_node.right_node
    return leaf_node

# Root -> Left -> Right
def preorder_travel(root_node) -> None:
    stack = [root_node]
    while True:
        try:
            node = stack.pop()
        except IndexError:
            break
        print(node.value)
        if node.right_node is not None:
            stack.append(node.right_node)
        if node.left_node is not None:
            stack.append(node.left_node)

# Left -> Root -> Right
def inorder_travel(root_node) -> None:
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
        print(node.value)
        node = node.right_node

# Left -> Right -> Root
def postorder_travel(root_node) -> None:
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
            print(node.value)
            node = None
        else:
            tmp_node = node.right_node
            node.right_node = None
            stack.append(node)
            node = tmp_node

def solution() -> None:
    root_node = None
    while True:
        try:
            A = int(input())
            if root_node is None:
                root_node = Node(A)
            else:
                found_node = find_leaf_node(root_node, A)
                node = Node(A)
                found_node.add_child(node)
        except EOFError:
            break
    print('[ preorder_travel ]')
    preorder_travel(root_node)
    print('[ inorder_travel ]')
    inorder_travel(root_node)
    print('[ postorder_travel ]')
    postorder_travel(root_node)
    return

# Input 오류는 고려하지 않는다.
if __name__ == '__main__':
    solution()
