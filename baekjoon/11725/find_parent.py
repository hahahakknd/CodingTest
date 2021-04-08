def next_index(index) -> int:
    if index == len(LINKS)-1:
        return 0
    else:
        return index + 1

def solution() -> None:
    index = 0
    match_parent = 0
    while len(LINKS) != match_parent:
        link = LINKS[index]
        node_1 = link[0]
        if node_1 == -1:
            index = next_index(index)
            continue
        node_2 = link[1]
        if node_1 == 1:
            NODES[node_2] = node_1
            LINKS[index][0] = -1
            match_parent += 1
        elif node_2 == 1:
            NODES[node_1] = node_2
            LINKS[index][0] = -1
            match_parent += 1
        elif NODES.get(node_1) != 0:
            NODES[node_2] = node_1
            LINKS[index][0] = -1
            match_parent += 1
        elif NODES.get(node_2) != 0:
            NODES[node_1] = node_2
            LINKS[index][0] = -1
            match_parent += 1
        index = next_index(index)

    for parent in NODES.values():
        if parent != 0:
            print(parent)
    return

# Input 오류는 고려하지 않는다.
if __name__ == '__main__':
    global NODES, LINKS
    NODES = {}
    LINKS = []
    node_count = int(input())
    NODES[1] = 0
    for i in range(1, node_count):
        NODES[i+1] = 0
        input_data = input().split(' ')
        LINKS.append([int(input_data[0]), int(input_data[1])])
    solution()
    # for i in range(1,7+1):
    #     NODES[i] = 0
    # LINKS.append([1,6])
    # LINKS.append([6,3])
    # LINKS.append([3,5])
    # LINKS.append([4,1])
    # LINKS.append([2,4])
    # LINKS.append([4,7])
    # solution()
    # print('----------------')
    # NODES.clear()
    # LINKS.clear()
    # for i in range(1,7+1):
    #     NODES[i] = 0
    # LINKS.append([6,3])
    # LINKS.append([4,7])
    # LINKS.append([4,1])
    # LINKS.append([1,6])
    # LINKS.append([2,4])
    # LINKS.append([3,5])
    # solution()
    # print('----------------')
    # NODES.clear()
    # LINKS.clear()
    # for i in range(1,12+1):
    #     NODES[i] = 0
    # LINKS.append([1,2])
    # LINKS.append([1,3])
    # LINKS.append([2,4])
    # LINKS.append([3,5])
    # LINKS.append([3,6])
    # LINKS.append([4,7])
    # LINKS.append([4,8])
    # LINKS.append([5,9])
    # LINKS.append([5,10])
    # LINKS.append([6,11])
    # LINKS.append([6,12])
    # solution()
