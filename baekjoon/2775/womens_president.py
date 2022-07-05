import sys

# 3층 - 01  05  15  35  70  126 ...
# 2층 - 01  04  10  20  35  56  ...
# 1층 - 01  03  06  10  15  21  ...
# 0층 - 01  02  03  04  05  06  ...

def resident_count(k: int, n: int) -> int:
    if n == 1:
        return 1

    if k == 0:
        return n

    left_resident_count: int = resident_count(k, n-1)
    down_resident_count: int = resident_count(k-1, n)

    return left_resident_count + down_resident_count

def solution(testcase: list) -> None:
    for test in testcase:
        print(resident_count(test[0], test[1]))
    return

# Input 오류는 고려하지 않는다.
if __name__ == '__main__':
    input_data = sys.stdin.readline().rstrip().split(' ')
    test_list: list = []
    count: int = int(input_data[0])
    for num in range(count):
        test_list.append([int(sys.stdin.readline().rstrip().split(' ')[0]),
                          int(sys.stdin.readline().rstrip().split(' ')[0])])
    solution(test_list)
