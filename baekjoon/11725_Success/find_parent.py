import sys

# 부모를 찾는다는 접근법으로 풀었다.
# 결과는 시간초과....
# 장원형 풀이는 자식을 찾는다 라는 접근법으로 풀었다.
# 발상의 전환이 필요하다.

def what_is_root(node) -> int:
    global NODES, STACK
    up_node = NODES[node]
    before_node = -1
    while True:
        if up_node == 0:
            return 0
        if up_node == 1:
            return 1
        if NODES[up_node] == before_node:
            return 0
        before_node = up_node
        up_node = NODES[up_node]

def find_parent(node_1, node_2) -> None:
    global NODES, STACK
    if node_1 == 1:
        NODES[node_2] = node_1
        return
    if node_2 == 1:
        NODES[node_1] = node_2
        return
    if what_is_root(node_1) == 0:
        NODES[node_1] = node_2
    if what_is_root(node_2) == 0:
        NODES[node_2] = node_1

def solution() -> None:
    global NODES, STACK
    for parent in NODES.values():
        if parent != 0:
            print(parent)

# Input 오류는 고려하지 않는다.
if __name__ == '__main__':
    global NODES, STACK
    NODES = {}
    STACK = []
    node_count = int(sys.stdin.readline().rstrip())
    for i in range(1, node_count+1):
        NODES[i] = 0
    for i in range(1, node_count):
        input_data = sys.stdin.readline().rstrip().split(' ')
        find_parent(int(input_data[0]), int(input_data[1]))
    solution()
    # for i in range(1,7+1):
    #     NODES[i] = 0
    # find_parent(1,6)
    # find_parent(6,3)
    # find_parent(3,5)
    # find_parent(4,1)
    # find_parent(2,4)
    # find_parent(4,7)
    # solution()
    # print('----------------')
    # NODES.clear()
    # STACK.clear()
    # for i in range(1,11+1):
    #     NODES[i] = 0
    # find_parent(1,3)
    # find_parent(9,10)
    # find_parent(1,9)
    # find_parent(3,7)
    # find_parent(3,4)
    # find_parent(7,6)
    # find_parent(2,11)
    # find_parent(5,2)
    # find_parent(7,5)
    # find_parent(7,8)
    # solution()
    # print('----------------')
    # NODES.clear()
    # STACK.clear()
    # for i in range(1,12+1):
    #     NODES[i] = 0
    # find_parent(1,2)
    # find_parent(1,3)
    # find_parent(2,4)
    # find_parent(3,5)
    # find_parent(3,6)
    # find_parent(4,7)
    # find_parent(4,8)
    # find_parent(5,9)
    # find_parent(5,10)
    # find_parent(6,11)
    # find_parent(6,12)
    # solution()
