import sys

#
# 무식하게 다 계산하는 방법
# 0: 없음, 1: 있음
#
cache: list = [0 for i in range(0, 10000)]

def solution():
    n: int = 1
    number: int = 0
    while n <= 9972:
        a = n      // 1000  # 1000의 자리
        b = n%1000 // 100   # 100의 자리
        c = n%100  // 10    # 10의 자리
        d = n%10            # 1의 자리
        number = n + a + b + c + d
        # print(str(number) + ', d(' + str(n) + ')')
        if number <= 10000:
            cache[number-1] = 1
        n += 1

# Input 오류는 고려하지 않는다.
if __name__ == '__main__':
    solution()
    loop_count: int = len(cache)
    for i in range(0, loop_count):
        if cache[i] == 0:
            print(i+1)
