class Node:
    def __init__(self, parent_node, value) -> None:
        self.value = value
        self.parent_node = parent_node
        self.left_node = None
        self.right_node = None

    def add_child(self, child_node) -> None:
        if self.value > child_node.value:
            self.left_node = child_node
        else:
            self.right_node = child_node

    def is_left_node(self, node) -> bool:
        if self.left_node is not None and self.left_node.value == node.value:
            return True
        return False

    def to_string(self) -> str:
        msg = 'value:' + str(self.value)
        if self.parent_node is None:
            msg += ', parent:None'
        else:
            msg += (', parent:' + str(self.parent_node.value))

        if self.left_node is None:
            msg += ', left_node:None'
        else:
            msg += (', left_node:' + str(self.left_node.value))

        if self.right_node is None:
            msg += ', right_node:None'
        else:
            msg += (', right_node:' + str(self.right_node.value))

        return msg


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

def find_start_node_for_back_travel(node) -> Node:
    start_node = node
    while True:
        if start_node.left_node is None and start_node.right_node is None:
            break
        if start_node.left_node is not None:
            start_node = start_node.left_node
            continue
        if start_node.right_node is not None:
            start_node = start_node.right_node
            continue
    return start_node

def back_travel(root_node) -> None:
    stack = []

    while True:
        stack.append(root_node.value)


        print(travel_node.value)
        if travel_node.parent_node.parent_node is None:
            break
        if travel_node.parent_node.is_left_node(travel_node) is not True  \
                or travel_node.parent_node.right_node is None:
            travel_node = travel_node.parent_node
            continue
        travel_node = travel_node.parent_node.right_node

def solution() -> None:
    root_node = None
    while True:
        try:
            A = int(input())
            if root_node is None:
                root_node = Node(None, A)
            else:
                found_node = find_leaf_node(root_node, A)
                node = Node(found_node, A)
                found_node.add_child(node)
        except EOFError:
            break
    back_travel(root_node)
    return

# Input 오류는 고려하지 않는다.
if __name__ == '__main__':
    solution()
