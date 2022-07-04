import sys

# 1행: 1/1
# 2행: 1/2  2/1
# 3행: 3/1  2/2  1/3
# 4행: 1/4  2/3  3/2  4/1
# 5행: 5/1  4/2  3/3  2/4  1/5
# 6행: 1/6  2/5  3/4  4/3  5/2  6/1
# 7행: 7/1  6/2  5/3  4/4  3/5  2/6  1/7
#
# n(n+1)/2 > x
#
# 홀수행: 분모는 최대값으로 시작하고 1씩 감소, 분자는 1 부터 시작하고 1씩 증가
# 짝수행: 분모는 1 부터 시작하고 1씩 증가, 분자는 최대값으로 시작하고 1씩 감소
def solution(x: int) -> None:
    n: int = 1

    # x 가 포함되는 행을 찾는다.
    while True:
        max_sum: int = n*(n+1)//2  # 항상 정수가 나온다.
        if max_sum >= x:
            break
        n += 1

    # 얼만큼 더하고 뺄거냐
    gap: int = max_sum - x  # 항상 0 과 양수

    # n 이 홀수인지 짝수인지 판단한다.
    is_odd_number: bool = not n%2 == 0

    if is_odd_number:  # 홀수
        denominator: int = n - gap  # 분모
        numerator: int = 1 + gap    # 분자
    else:  # 짝수
        denominator: int = 1 + gap
        numerator: int = n - gap

    print(str(numerator) + "/" + str(denominator))
    return

# Input 오류는 고려하지 않는다.
if __name__ == '__main__':
    input_data = sys.stdin.readline().rstrip().split(' ')
    solution(int(input_data[0]))
