# 이것도 시간초과가 발생한다...
# Stack 을 쓰는 방법은 시간초과가 날 수밖에 없나???
class Node:
    def __init__(self, parent_number, parent_max_num, number, value) -> None:
        self.parent_number = parent_number
        self.number = number
        self.value = value
        self.max_sum = parent_max_num + value

def solution() -> None:
    stairs_size = len(stairs)
    stack = []
    stack.append(Node(-1,0,0,stairs[0]))
    max_sum = 0

    while True:
        try:
            node = stack.pop()
            if node.number+2 < stairs_size:
                stack.append(Node(node.number, node.max_sum, node.number+2, stairs[node.number+2]))
            if node.number+1 < stairs_size:
                if node.parent_number == -1 or node.parent_number != node.number-1:
                    stack.append(Node(node.number, node.max_sum, node.number+1, stairs[node.number+1]))
            if node.number+1 == stairs_size and max_sum < node.max_sum:
                max_sum = node.max_sum
        except IndexError:
            break

    print(max_sum)
    return

# Input 오류는 고려하지 않는다.
if __name__ == '__main__':
    stairs = []
    loop_count = int(input())
    for _ in range(0, loop_count):
        stairs.append(int(input()))
    solution()
    # stairs = [10,20,15,25,10,20]
    # solution()
