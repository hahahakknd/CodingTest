# 리커시브 에러가 발생한다.
class Node:
    def __init__(self, value) -> None:
        self._value = value
        self._left_node = None
        self._right_node = None

    def add_child(self, value) -> None:
        if self._value == value:
            raise Exception

        if self._value > value:
            if self._left_node is not None:
                self._left_node.add_child(value)
            else:
                self._left_node = Node(value)
        else:
            if self._right_node is not None:
                self._right_node.add_child(value)
            else:
                self._right_node = Node(value)

    def back_travel(self) -> None:
        if self._left_node is not None:
            self._left_node.back_travel()

        if self._right_node is not None:
            self._right_node.back_travel()

        print(self._value)

def solution() -> None:
    root_node = None
    while True:
        try:
            A = int(input())
            if root_node is None:
                root_node = Node(A)
            else:
                root_node.add_child(A)
        except EOFError:
            break
    root_node.back_travel()
    return

# Input 오류는 고려하지 않는다.
if __name__ == '__main__':
    solution()
