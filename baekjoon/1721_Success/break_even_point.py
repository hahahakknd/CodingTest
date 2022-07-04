import sys

# 21억 이하의 자연수라는 의미는 int32 를 input 으로 받는다는 의미이다.
# 고정비용: A, 가변비용: B, 노트북가격: C, 판매대수: D
# C*D = A+B*D --> (C*D)-(B*D) = A --> (C-B)*D = A --> D = A/(C-B)
# Python 에서 '/' 는 부동소수점 나눗셈이고, '//' 는 정수 나눗셈이다.
def solution(fixed_cost: int, variable_cost: int, notebook_cost: int) -> None:
    # denominator 는 분모라는 의미
    denominator: int = notebook_cost - variable_cost

    # 손익분기점이 나올 수가 없음
    if denominator <= 0:
        print("-1")
        return

    result: int = fixed_cost // denominator

    # 공식의 결과보다 무조건 1대를 더 팔아야 손익분기점이다.
    sales: int = result + 1

    print(sales)
    return

# Input 오류는 고려하지 않는다.
if __name__ == '__main__':
    input_data = sys.stdin.readline().rstrip().split(' ')
    solution(int(input_data[0]), int(input_data[1]), int(input_data[2]))
