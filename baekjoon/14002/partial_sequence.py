import sys

#
# 아래 코드는 동작은 하는데 Recursive error 가 발생한다.
# 재귀로 Tree 를 만드니까 재귀함수 호출이 너무 많아서 Error 가 발생한다... ㅠㅠ
#
# class Node:
#     NONE: int = 0
#     ASC: int = 1
#     DEC: int = 2

#     def __init__(self, __nodes: list) -> None:
#         self._value: int = __nodes[0]
#         self._sub_nodes: list = []
#         for i in range(1, len(__nodes)):
#             self._sub_nodes.append(Node(__nodes[i:]))
#         return

#     def find_max_depth(self, __order: int) -> int:
#         depth: int = 1
#         sub_depth: int = 0
#         for sub_node in self._sub_nodes:
#             if (__order == self.ASC) \
#                     and (self._value >= sub_node._value):
#                 continue
#             elif (__order == self.DEC) \
#                     and (self._value <= sub_node._value):
#                 continue

#             tmp_depth: int = sub_node.find_max_depth(__order)
#             if sub_depth < tmp_depth:
#                 sub_depth = tmp_depth
#         return depth + sub_depth

# def make_tree(num_seq: list) -> Node:
#     return Node(num_seq)

# def solution(num_seq: list) -> None:
#     start_node: Node = make_tree(num_seq)
#     print(start_node.find_max_depth(Node.ASC))
#     return

class BinaryNode:
    def __init__(self, __my_value: int, __left_value: BinaryNode, __right_value: int) -> None:
        self._value: int = __my_value

def make_tree(num_seq: list) -> BinaryNode:
    return Node(num_seq)

def solution(num_seq: list) -> None:
    return

# Input 오류는 고려하지 않는다.
if __name__ == '__main__':
    input()  # 수열 크기는 버린다.
    num_sequence: list = [int(number) for number in input().split(' ')]
    solution(num_sequence)
