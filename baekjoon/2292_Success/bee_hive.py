import sys

#  1개 - 01
#  6개 - 02  03  04  05  06  07
# 12개 - 08  09  10  11  12  13  14  15  16  17  18  19
# 18개 - 20  21  22  23  24  25  26  27  28  29  30  31  32  33  34  35  36  37
#
# a_n = a_1 + (n-1)d
#
# a_1 = 6
# d = d
# a_n = 6 + 6(n-1) = 6n
#
# s_n = n(a_1 + a_n)/2
# s_n = n(6 + 6n)/2
# s_n = 3n + 3n^2 = 3n(n+1)

# def solution(number: int) -> None:
#     if number == 1:
#         print(1)
#         return

#     n: int = 1
#     while True:
#         if (3*n*(n+1)) + 1 >= number:
#             break
#         n += 1

#     print(n+1)

def solution(number: int) -> None:
    if number == 1:
        print(1)
        return

    n: int = 1
    sum: int = 1
    while sum < number:
        sum += 6*n
        n += 1

    print(n)

# Input 오류는 고려하지 않는다.
if __name__ == '__main__':
    input_data = sys.stdin.readline().rstrip().split(' ')
    solution(int(input_data[0]))
