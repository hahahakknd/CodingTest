def stack_push(item) -> None:
    STACK.append(item)
    OPRATORS.append('+')

def stack_pop() -> None:
    STACK.pop()
    OPRATORS.append('-')

def stack_last() -> int:
    return STACK[len(STACK)-1]

def stack_empty() -> bool:
    return True if len(STACK) == 0 else False

def solution() -> None:
    ans_pos = 0
    for i in range(1,SEQ_NUM+1):
        if ANSWER[ans_pos] > i:
            stack_push(i)
            continue

        stack_push(i)
        stack_pop()
        ans_pos += 1

        while True:
            if stack_empty() == True:
                break
            if stack_last() < ANSWER[ans_pos]:
                break
            if stack_last() > ANSWER[ans_pos]:
                print('NO')
                return
            stack_pop()
            ans_pos += 1

    for op in OPRATORS:
        print(op)
    return

# Input 오류는 고려하지 않는다.
if __name__ == '__main__':
    global STACK, ANSWER, SEQ_NUM, OPRATORS
    STACK = []
    OPRATORS = []
    ANSWER = []
    SEQ_NUM = int(input())
    for _ in range(SEQ_NUM):
        ANSWER.append(int(input()))
    solution()
    # ANSWER = [4,3,6,8,7,5,2,1]
    # SEQ_NUM = 8
    # solution()
    # ANSWER = [1,2,5,3,4]
    # SEQ_NUM = 5
    # solution()
