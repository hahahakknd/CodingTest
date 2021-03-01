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

#
# Index tree 는 Full binary tree 로 구성이 된다.
#
# Index tree 의 Max depth
# -> max_depth = ???
#
# Index tree 를 위해 필요한 Array size, Max depth 는 1보다 작으면 안된다.
# -> array_size = 3 + 4*(2^(max_depth-1) - 1)
#               = 3 + 2^(max_depth+1) - 4
#               = 2^(max_depth+1) - 1
#
# Node 위치, Depth 는 항상 0보다 커야한다.
# -> left_node_pos = 2*parent_pos + 1
# -> right_node_pos = 2*parent_pos + 2
#
# 해당 Depth 의 시작 및 종료 위치, Depth 는 항상 0보다 커야한다.
# -> depth_start_pos = 2^depth - 1
# -> depth_end_pos = 2^(depth+1) - 2
#
# class IndexTree:
#     def __init__(self, __nodes: list) -> None:
#         if len(__nodes) == 0:
#             raise Exception('Invalid argument. Size of nodes is 0.')

#         # Get max depth.
#         self._max_depth: int = 1
#         while True:
#             if (2**self._max_depth) >= len(__nodes):
#                 break
#             self._max_depth += 1

#         # Make list for index tree.
#         self._index_tree: list = [-1 for value in range(2**(self._max_depth+1) - 1)]

#         #
#         # Make index tree
#         #
#         leaf_node_start_pos = 2**self._max_depth - 1
#         for i in range(0, len(__nodes)):
#             self._index_tree[leaf_node_start_pos + i] = __nodes[i]

#         for depth in range(self._max_depth, 0, -1):
#             depth_start_pos: int = 2**depth - 1
#             depth_end_pos: int = 2**(depth+1) - 2
#             parent_pos: int = (depth_start_pos-1) // 2
#             for pos in range(depth_start_pos, depth_end_pos+1, 2):
#                 left_value: int = self._index_tree[pos]
#                 if left_value == -1:
#                     continue
#                 right_value: int = self._index_tree[pos+1]
#                 # print('parent_pos:' + str(parent_pos) + ', left_value:' + str(left_value) + ', right_value:' + str(right_value))
#                 if left_value >= right_value:
#                     self._index_tree[parent_pos] = left_value
#                 else:
#                     self._index_tree[parent_pos] = right_value
#                 parent_pos += 1

#     def print_tree(self) -> None:
#         print(self._index_tree[:1])
#         for depth in range(1, self._max_depth+1):
#             depth_start_pos: int = 2**depth - 1
#             depth_end_pos: int = 2**(depth+1) - 2
#             print(self._index_tree[depth_start_pos:depth_end_pos+1])

#     def find_next_greater_num(self, cur_num: int) -> int:
#         stack: list = [[self._index_tree[0], 0, 0]]  # value, postion, depth
#         next_greater_num: int = -1

#         while len(stack) != 0:
#             node: list = stack.pop()
#             if cur_num > node[0]:
#                 continue

#             next_depth: int = node[2] + 1
#             if self._max_depth < next_depth:  # Leaf node
#                 if next_greater_num == -1:
#                     next_greater_num = node[0]
#                 elif next_greater_num > node[0]:
#                     next_greater_num = node[0]
#                 continue

#             right_child_pos: int = 2*node[1] + 1
#             right_child_num: int = self._index_tree[right_child_pos]
#             if right_child_num > cur_num:
#                 stack.append([self._index_tree[right_child_pos], right_child_pos, next_depth])

#             left_child_pos: int = 2*node[1] + 2
#             left_child_num: int = self._index_tree[left_child_pos]
#             if left_child_num > cur_num:
#                 stack.append([self._index_tree[left_child_pos], left_child_pos, next_depth])

#         return next_greater_num

# def solution(num_seq: list) -> None:
#     index_tree: IndexTree = IndexTree(num_seq)
#     index_tree.print_tree()

#     answer: list = []
#     tmp_answer: list = []
#     for i in range(0, len(num_seq)):
#         tmp_answer.clear()
#         tmp_answer.append(num_seq[i])

#         while True:
#             next_greater_num: int = index_tree.find_next_greater_num(tmp_answer[len(tmp_answer)-1])
#             if next_greater_num == -1:
#                 break
#             tmp_answer.append(next_greater_num)

#         if len(answer) < len(tmp_answer):
#             answer = tmp_answer.copy()

#     print(len(answer))
#     print(answer)
#     return

#
# Timeout 발생한다.
#
# class Node:
#     def __init__(self, __value: int, __postion: int) -> None:
#         self.value: int = __value
#         self.postion: int = __postion
#         self.sub_nodes: list = []
#         return

#     def set_sub_nodes(self, __sub_nodes: list) -> None:
#         self.sub_nodes += __sub_nodes
#         return

#     def find_max_list(self) -> list:
#         value_list: list = []
#         for sub_node in self.sub_nodes:
#             if self.value >= sub_node.value:
#                 continue
#             tmp_list: list = sub_node.find_max_list()
#             if len(value_list) < len(tmp_list):
#                 value_list = tmp_list

#         value_list.insert(0, self.value)
#         return value_list

#     def find_max_depth(self) -> int:
#         sub_depth: int = 0
#         for sub_node in self.sub_nodes:
#             if self.value >= sub_node.value:
#                 continue

#             tmp_depth: int = sub_node.find_max_depth()
#             if sub_depth < tmp_depth:
#                 sub_depth = tmp_depth
#         return sub_depth + 1

# def make_tree(_num_seq: list, _start_pos: int) -> Node:
#     root_node: Node = Node(_num_seq[_start_pos], _start_pos)
#     stack: list = [root_node]

#     while len(stack) != 0:
#         node: Node = stack.pop()
#         if len(_num_seq) <= (node.postion+1):
#             continue

#         sub_nodes: list = []
#         for i in range(node.postion+1, len(_num_seq)):
#             if _num_seq[i] > node.value:
#                 sub_nodes.append(Node(_num_seq[i], i))

#         if len(sub_nodes) == 0:
#             continue

#         node.sub_nodes = sub_nodes.copy()
#         stack += sub_nodes

#     return root_node

# def solution(num_seq: list) -> None:
#     org_list_size: int = len(num_seq)
#     answer: list = []
#     answer_depth: int = 0
#     for i in range(0, org_list_size):
#         if answer_depth >= (org_list_size-i):
#             break

#         node: Node = make_tree(num_seq, i)
#         tmp_answer: list = node.find_max_list()

#         if len(answer) >= len(tmp_answer):
#             continue

#         answer = tmp_answer
#         answer_depth = len(tmp_answer)

#     print(answer_depth)
#     for i in range(0, answer_depth-1):
#         print(answer[i], end=' ')
#     print(answer[answer_depth-1])

#     return

def make_max_list(sequence: list, caches: list) -> list:
    max_list: list = [sequence[0]]
    max_value: int = sequence[0]

    tmp_list: list = []
    for cache in caches:
        if max_value < cache[0]:
            if len(tmp_list) < len(cache):
                tmp_list = cache
                continue

    if tmp_list != 0:
        return max_list + tmp_list

    for value in sequence[1:]:
        if max_value >= value:
            continue
        max_list.append(value)
        max_value = value

    return max_list

def solution(num_seq: list) -> None:
    caches: list = [[] for _ in num_seq]
    answer: list = []

    caches[len(caches)-1] = [num_seq[len(num_seq)-1]]
    answer = caches[len(caches)-1]

    for i in range(len(num_seq)-2, -1, -1):
        caches[i] = make_max_list(num_seq[i:], caches[i+1:])
        if len(answer) < len(caches[i]):
            answer = caches[i]

    answer_size: int = len(answer)
    print(answer_size)
    for i in range(0, answer_size-1):
        print(answer[i], end=' ')
    print(answer[answer_size-1])

    return

# Input 오류는 고려하지 않는다.
if __name__ == '__main__':
    input()  # 수열 크기는 버린다.
    num_sequence: list = [int(number) for number in input().split(' ')]
    solution(num_sequence)
