import sys

def solution() -> None:
    global NODES, STACK, RELATIONS
    STACK.append(1)
    while len(STACK) != 0:
        node = STACK.pop()
        for child in RELATIONS[node]:
            if child != 1 and NODES[child] == 0:
                NODES[child] = node
                STACK.append(child)
    for parent in NODES.values():
        if parent != 0:
            print(parent)

# Input 오류는 고려하지 않는다.
if __name__ == '__main__':
    global NODES, STACK, RELATIONS
    STACK = []
    NODES = {}
    RELATIONS = {}
    node_count = int(sys.stdin.readline().rstrip())
    for i in range(1, node_count+1):
        NODES[i] = 0
        RELATIONS[i] = []
    for _ in range(1, node_count):
        input_data = sys.stdin.readline().rstrip().split(' ')
        left = int(input_data[0])
        right = int(input_data[1])
        RELATIONS[left].append(right)
        RELATIONS[right].append(left)
    solution()
    # for i in range(1,7+1):
    #     NODES[i] = 0
    #     RELATIONS[i] = []
    # RELATIONS[1].append(6)
    # RELATIONS[6].append(1)
    # RELATIONS[6].append(3)
    # RELATIONS[3].append(6)
    # RELATIONS[3].append(5)
    # RELATIONS[5].append(3)
    # RELATIONS[4].append(1)
    # RELATIONS[1].append(4)
    # RELATIONS[2].append(4)
    # RELATIONS[4].append(2)
    # RELATIONS[4].append(7)
    # RELATIONS[7].append(4)
    # solution()
    # print('----------------')
    # NODES.clear()
    # STACK.clear()
    # for i in range(1,11+1):
    #     NODES[i] = 0
    #     RELATIONS[i] = []
    # RELATIONS[1].append(3)
    # RELATIONS[3].append(1)
    # RELATIONS[9].append(10)
    # RELATIONS[10].append(9)
    # RELATIONS[1].append(9)
    # RELATIONS[9].append(1)
    # RELATIONS[3].append(7)
    # RELATIONS[7].append(3)
    # RELATIONS[3].append(4)
    # RELATIONS[4].append(3)
    # RELATIONS[7].append(6)
    # RELATIONS[6].append(7)
    # RELATIONS[2].append(11)
    # RELATIONS[11].append(2)
    # RELATIONS[5].append(2)
    # RELATIONS[2].append(5)
    # RELATIONS[7].append(5)
    # RELATIONS[5].append(7)
    # RELATIONS[7].append(8)
    # RELATIONS[8].append(7)
    # solution()
