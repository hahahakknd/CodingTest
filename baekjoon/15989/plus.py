import sys

def solution(number: int, max_num: int) -> int:
    if max_num == 2:
        return (number//max_num) + 1

    count: int = 0
    for i in range(0, (number//max_num)+1):
        count += solution(number-(max_num*i), max_num-1)

    return count

# Input 오류는 고려하지 않는다.
if __name__ == '__main__':
    loop_count: int = int(input())
    for i in range(0, loop_count):
        num: int = int(input())
        print(str(solution(num, 3)))
