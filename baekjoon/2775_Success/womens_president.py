import sys

# 3층 - 01  05  15  35  70  126 ...
# 2층 - 01  04  10  20  35  56  ...
# 1층 - 01  03  06  10  15  21  ...  n(n+1)/2
# 0층 - 01  02  03  04  05  06  ...

# 재귀는 Timeout 발생
# def resident_count(k: int, n: int) -> int:
#     if n == 1:
#         return 1
#
#     if k == 0:
#         return n
#
#     left_resident_count: int = resident_count(k, n-1)
#     down_resident_count: int = resident_count(k-1, n)
#
#     return left_resident_count + down_resident_count

# Testcase 의 갯수 T 가 주어지는데, T 의 값만큼 중복연산하는 것은 불필요하다.
# 따라서 최대행렬까지 데이터를 구성한 다음에 정답을 조회만 하는 방향으로 구현한다.
def resident_map(max_k: int, max_n: int) -> list:
    # 1층에 대한 초기화
    floor_map: list = []
    floor: list = []
    for num in range(1, max_n+1):
        floor.append(num*(num+1)//2)
    floor_map.append(floor.copy())

    if max_k == 1:
        return floor_map

    for floor_number in range(1, max_k):
        floor.clear()
        for room_number in range(0, max_n):
            sum_down_resident: int = 0
            for down_floor_room_number in range(0, room_number+1):
                sum_down_resident += floor_map[floor_number-1][down_floor_room_number]
            floor.append(sum_down_resident)
        floor_map.append(floor.copy())

    return floor_map

def solution(testcase: list) -> None:
    max_k: int = 0
    max_n: int = 0
    for test in testcase:
        if max_k < test[0]:
            max_k = test[0]
        if max_n < test[1]:
            max_n = test[1]

    resident_table: list = resident_map(max_k, max_n)

    for test in testcase:
        print(resident_table[test[0]-1][test[1]-1])
    return

# Input 오류는 고려하지 않는다.
if __name__ == '__main__':
    input_data = sys.stdin.readline().rstrip().split(' ')
    test_list: list = []
    count: int = int(input_data[0])
    for _ in range(count):
        test_list.append([int(sys.stdin.readline().rstrip().split(' ')[0]),
                          int(sys.stdin.readline().rstrip().split(' ')[0])])
    solution(test_list)
