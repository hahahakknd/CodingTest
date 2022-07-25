import sys

# 1 부터 n 까지의 수들 중에서 모든 소수를 찾는 방법: 에라토스테네스의 체
# n 의 루트를 구하는 방법: [1] n**(1/2) [2] Math.sqrt(n)
# n 이 소수인지 판단하는 방법: 2 부터 루트n 까지의 소수들로 나누어 떨어지지 않으면 소수
#
# 본 문제에서는 10000 이하의 자연수 중에서 소수를 찾기 때문에 "에라토스테네스의 체" 방식을 사용한다.
def solution(m: int, n: int) -> None:
    # "에라토스테네스의 체" 구성
    sieve: list = [num+1 for num in range(10000)]

    # 1 은 소수가 아니니 제외
    sieve[0] = 0

    # "에라토스테네스의 체" 에서 소수가 아닌 놈들 제외
    for num in sieve:
        if num == 0:
            continue

        position: int = num-1

        for inner_num in sieve[num:]:
            position += 1

            if inner_num == 0:
                continue

            if inner_num%num == 0:
                sieve[position] = 0

    print(sieve)

    # m 이상 n 이하의 자연수 중에서 소수인 것들을 찾아 합과 최소값을 구한다.
    sum_prime_number: int  = 0
    min_prime_number: int  = 0

    if m == n:
        sum_prime_number = sieve[m-1]
        min_prime_number = sieve[m-1]
    else:
        for num in sieve[m-1:n-1]:
            if num == 0:
                continue

            if min_prime_number == 0:
                min_prime_number = num

            sum_prime_number += num

    if min_prime_number == 0:
        print(-1)
    else:
        print(sum_prime_number)
        print(min_prime_number)

# Input 오류는 고려하지 않는다.
if __name__ == '__main__':
    m = sys.stdin.readline().rstrip().split(' ')
    n = sys.stdin.readline().rstrip().split(' ')
    solution(int(m[0]), int(n[0]))
