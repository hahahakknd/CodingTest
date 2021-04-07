def solution(vps) -> None:
    stack = []
    for c in vps:
        if c == '(':
            stack.append(c)
        else:
            try:
                stack.pop()
            except IndexError:
                print('NO')
                return
    if len(stack) != 0:
        print('NO')
    else:
        print('YES')
    return

# Input 오류는 고려하지 않는다.
if __name__ == '__main__':
    loop_count = int(input())
    for _ in range(loop_count):
        solution(input())
    # solution(['(','(',')',')','(',')',')'])
    # solution(['(','(','(','(',')','(',')',')','(',')'])
    # solution(['(','(',')','(',')',')','(','(','(',')',')',')'])
    # solution(['(','(','(',')','(',')','(','(',')',')',')','(','(','(','(',')',')',')',')','(',')'])
    # solution(['(',')','(',')','(',')','(',')','(','(',')','(',')','(',')',')','(',')'])
    # solution(['(','(',')','(','(','(',')',')','(',')','('])
