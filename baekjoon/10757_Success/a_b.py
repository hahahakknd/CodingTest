import sys

# 파이썬에서는 범위를 벗어나는 큰 수에 대한 연산을 지원한다. (미리 구현되어 있음)
def solution(a: int, b: int) -> None:
    print(a+b)
    return

# Input 오류는 고려하지 않는다.
if __name__ == '__main__':
    input_data = sys.stdin.readline().rstrip().split(' ')
    solution(int(input_data[0]), int(input_data[1]))
