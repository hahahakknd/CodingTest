import sys

def is_open(nation_one, nation_two) -> bool:
    global L, R
    diff_num = abs(nation_one-nation_two)
    if diff_num < L or diff_num > R:
        return False
    return True

def move_population() -> bool:
    global N, NATIONS
    directions = [[-1,0],[0,-1],[0,1],[1,0]]
    used_nations = [[False for _ in range(N)] for _ in range(N)]
    unions = []
    for i in range(N):
        for j in range(N):
            if used_nations[i][j]:
                continue
            result = [[i,j]]
            used_nations[i][j] = True
            stack = [[i,j]]
            while len(stack) != 0:
                tmp_point = stack.pop()
                nation_one = NATIONS[tmp_point[0]][tmp_point[1]]
                for direction in directions:
                    nation_two_point = [direction[0]+tmp_point[0], direction[1]+tmp_point[1]]
                    if     nation_two_point[0] < 0 or nation_two_point[0] >= N \
                        or nation_two_point[1] < 0 or nation_two_point[1] >= N \
                        or used_nations[nation_two_point[0]][nation_two_point[1]]:
                        continue
                    if is_open(nation_one, NATIONS[nation_two_point[0]][nation_two_point[1]]):
                        stack.append(nation_two_point)
                        result.append(nation_two_point)
                        used_nations[nation_two_point[0]][nation_two_point[1]] = True
            if len(result) > 1:
                unions.append(result)
    if len(unions) == 0:
        return False
    for union in unions:
        total_num = sum(union)
        divide_num = len(union)
        result_num = total_num//divide_num
        for point in union:
            NATIONS[point[0]][point[1]] = result_num
    return True

# Python3 에서는 시간초과...
# PyPy3 에서는 통과
def solution() -> None:
    global NATIONS
    count = 0
    while True:
        if not move_population():
            break
        count += 1
    print(count)
    return

# Input 오류는 고려하지 않는다.
if __name__ == '__main__':
    input_data = sys.stdin.readline().rstrip().split(' ')
    N = int(input_data[0])
    L = int(input_data[1])
    R = int(input_data[2])
    NATIONS = []
    for _ in range(N):
        NATIONS.append([int(x) for x in sys.stdin.readline().rstrip().split(' ')])
    solution()
    # N = 2
    # L = 20
    # R = 50
    # NATIONS = [[50,30],[20,40]]
    # solution()
    # N = 2
    # L = 40
    # R = 50
    # NATIONS = [[50,30],[20,40]]
    # solution()
    # N = 2
    # L = 20
    # R = 50
    # NATIONS = [[50,30],[30,40]]
    # solution()
    # N = 3
    # L = 5
    # R = 10
    # NATIONS = [[10,15,20],[20,30,25],[40,22,10]]
    # solution()
    # N = 4
    # L = 10
    # R = 50
    # NATIONS = [[10,100,20,90],[80,100,60,70],[70,20,30,40],[50,20,100,10]]
    # solution()
