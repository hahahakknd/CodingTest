import sys

# 각 자리수를 별개로 계산하는것을 의도했나???
# 그냥 더해도 Timeout 발생 안한다.....
def solution(a: int, b: int) -> None:
    print(a+b)
    return

# Input 오류는 고려하지 않는다.
if __name__ == '__main__':
    input_data = sys.stdin.readline().rstrip().split(' ')
    solution(int(input_data[0]), int(input_data[1]))
