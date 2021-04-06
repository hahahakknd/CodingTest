import sys

# B
# BA
# BAB
# BABBA
# BABBABAB
# BABBABABBABBA
#
# A
# 0 1 1 2 3 5
#
# B
# 1 1 2 3 5 8
#
#   A B
#     A B
# ---------------
# 0 1 1 2 3 5 8

# n번째 Fibo 를 찾으면 n번째, n+1번째 Fibo 가 리턴된다.
def find_fibo(fibo_size: int) -> tuple:
    first_fibo: int = 1
    second_fibo: int = 1

    for i in range(1, fibo_size):
        next_first_fibo: int = second_fibo
        second_fibo: int = first_fibo + second_fibo
        first_fibo = next_first_fibo

    return first_fibo, second_fibo

def find_A_and_B_count(click_count: int) -> tuple:
    if click_count == 1:
        return 0, 1

    return find_fibo(click_count-1)

# Input 오류는 고려하지 않는다.
if __name__ == '__main__':
    k: int = int(input())
    fibo: tuple = find_A_and_B_count(k)
    print(str(fibo[0]) + ' ' + str(fibo[1]))
