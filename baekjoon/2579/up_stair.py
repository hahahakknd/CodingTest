class Node:
    def __init__(self, parent, number, value) -> None:
        self.parent = parent
        self.number = number
        self.value = value
        self.max_sum = value
        if parent is not None:
            self.max_sum += parent.max_sum
        self.left = None
        self.right = None

    def add_child(self, node) -> None:
        if self.number == node.number-1:
            if self.parent is None or self.parent.number != self.number-1:
                self.left = node
        elif self.number == node.number-2:
            self.right = node

    def to_string(self) -> str:
        msg = 'parent:'
        if self.parent is None:
            msg += 'None'
        else:
            msg += str(self.parent.number)
        msg += ', number:' + str(self.number)
        msg += ', value:'+str(self.value)
        msg += ', max_num:'+str(self.max_sum)
        msg += ', left:'
        if self.left is None:
            msg += 'None'
        else:
            msg += str(self.left.number)
        msg += ', right:'
        if self.right is None:
            msg += 'None'
        else:
            msg += str(self.right.number)
        return msg

# Preorder Travel: Root -> Left -> Right
def find_max_sum(root_node) -> int:
    max_sum = 0
    stack = [root_node]
    while True:
        try:
            node = stack.pop()
        except IndexError:
            break
        if node.left is None and node.right is None:
            if max_sum < node.max_sum:
                max_sum = node.max_sum
        if node.right is not None:
            stack.append(node.right)
        if node.left is not None:
            stack.append(node.left)
    return max_sum

def solution() -> None:
    stairs_size = len(stairs)
    root_node = Node(None,0,stairs[0])
    stack = [root_node]

    while True:
        try:
            node = stack.pop()
            if node.number+1 < stairs_size:
                node.add_child(Node(node,node.number+1,stairs[node.number+1]))
            if node.number+2 < stairs_size:
                node.add_child(Node(node,node.number+2,stairs[node.number+2]))
            if node.right is not None:
                stack.append(node.right)
            if node.left is not None:
                stack.append(node.left)
        except IndexError:
            break

    print(find_max_sum(root_node))
    return

# Input 오류는 고려하지 않는다.
if __name__ == '__main__':
    stairs = []
    loop_count = int(input())
    for _ in range(0, loop_count):
        stairs.append(int(input()))
    solution()
