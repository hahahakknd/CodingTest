# 트리를 만들면 메모리 초과나 시간초과가 발생한다...
# 다른방법이 필요한 듯...
class Node:
    def __init__(self, parent, number, value) -> None:
        self.parent = parent
        self.number = number
        self.value = value
        self.max_sum = value
        if parent is not None:
            self.max_sum += parent.max_sum

    def to_string(self) -> str:
        msg = 'parent:'
        if self.parent is None:
            msg += 'None'
        else:
            msg += str(self.parent.number)
        msg += ', number:' + str(self.number)
        msg += ', value:'+str(self.value)
        msg += ', max_num:'+str(self.max_sum)
        return msg

def solution() -> None:
    stairs_size = len(stairs)
    stack = []
    stack.append(Node(None,0,stairs[0]))
    max_sum = 0

    while True:
        try:
            node = stack.pop()
            if node.number+2 < stairs_size:
                stack.append(Node(node,node.number+2,stairs[node.number+2]))
            if node.number+1 < stairs_size:
                if node.parent is None or node.parent.number != node.number-1:
                    stack.append(Node(node,node.number+1,stairs[node.number+1]))
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
