import sys

class Node:
    NONE: int = 0
    ASC: int = 1
    DEC: int = 2

    def __init__(self, __nodes: list) -> None:
        self._value: int = __nodes[0]
        self._sub_nodes: list = []
        for i in range(1, len(__nodes)):
            self._sub_nodes.append(Node(__nodes[i:]))
        return

    def find_max_depth(self, __order: int) -> int:
        depth: int = 1
        sub_depth: int = 0
        for sub_node in self._sub_nodes:
            if (__order == self.ASC) \
                    and (self._value >= sub_node._value):
                continue
            elif (__order == self.DEC) \
                    and (self._value <= sub_node._value):
                continue

            tmp_depth: int = sub_node.find_max_depth(__order)
            if sub_depth < tmp_depth:
                sub_depth = tmp_depth
        return depth + sub_depth

def make_tree(num_seq: list) -> Node:
    return Node(num_seq)

def solution(num_seq: list) -> None:
    start_node: Node = make_tree(num_seq)
    print(start_node.find_max_depth(Node.ASC))
    return

# Input 오류는 고려하지 않는다.
if __name__ == '__main__':
    input()  # 수열 크기는 버린다.
    num_sequence: list = [int(number) for number in input().split(' ')]
    solution(num_sequence)
