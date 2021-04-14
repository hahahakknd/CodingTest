import sys

def is_open(nation_one, nation_two) -> bool:
    global L, R
    diff_num = abs(nation_one-nation_two)
    if diff_num < L or diff_num > R:
        return False
    return True

def reset_unused_nation() -> None:
    global USED_NATIONS
    for i in range(len(USED_NATIONS)):
        for j in range(len(USED_NATIONS[i])):
            USED_NATIONS[i][j] = False

def find_unused_nation() -> list:
    global USED_NATIONS
    for i in range(len(USED_NATIONS)):
        for j in range(len(USED_NATIONS[i])):
            if USED_NATIONS[i][j] is False:
                return [i,j]
    return [-1,-1]

def is_found_unused_nation(point) -> bool:
    if point[0] == -1 and point[1] == -1:
        return False
    return True

def move_population(point) -> None:
    global N, USED_NATIONS, NATIONS, UNIONS
    directions = [[-1,0],[0,-1],[0,1],[1,0]]
    result = []
    stack = [point]
    while len(stack) != 0:
        tmp_point = stack.pop()
        result.append(tmp_point)
        USED_NATIONS[tmp_point[0]][tmp_point[1]] = True
        nation_one = NATIONS[tmp_point[0]][tmp_point[1]]
        for direction in directions:
            nation_two_point = [direction[0]+tmp_point[0], direction[1]+tmp_point[1]]
            if nation_two_point[0] < 0 or nation_two_point[0] >= N or nation_two_point[1] < 0 or nation_two_point[1] >= N or USED_NATIONS[nation_two_point[0]][nation_two_point[1]]:
                continue
            if is_open(nation_one, NATIONS[nation_two_point[0]][nation_two_point[1]]):
                stack.append([nation_two_point[0],nation_two_point[1]])
    divide_num = len(result)
    if divide_num == 1:
        return
    UNIONS.append(result)

def update_nations() -> None:
    global NATIONS, UNIONS
    for union in UNIONS:
        total_num = 0
        for point in union:
            total_num += NATIONS[point[0]][point[1]]
        divide_num = len(union)
        result_num = total_num//divide_num
        for point in union:
            NATIONS[point[0]][point[1]] = result_num

def print_matrix() -> None:
    global NATIONS
    for nation in NATIONS:
        print(nation)
    print('--------')

def solution() -> None:
    global NATIONS, UNIONS
    count = 0
    print_matrix()
    while True:
        point = find_unused_nation()
        if not is_found_unused_nation(point):
            if len(UNIONS) == 0:
                break
            update_nations()
            UNIONS.clear()
            count += 1
            reset_unused_nation()
            print_matrix()
            continue
        move_population(point)
    print(count)
    return

# Input 오류는 고려하지 않는다.
if __name__ == '__main__':
    # input_data = sys.stdin.readline().rstrip().split(' ')
    # N = int(input_data[0])
    # L = int(input_data[1])
    # R = int(input_data[2])
    # UNIONS = []
    # USED_NATIONS = [[False for _ in range(N)] for _ in range(N)]
    # NATIONS = []
    # for _ in range(N):
    #     NATIONS.append([int(x) for x in sys.stdin.readline().rstrip().split(' ')])
    # solution()
    # N = 2
    # L = 20
    # R = 50
    # UNIONS = []
    # USED_NATIONS = [[False for _ in range(N)] for _ in range(N)]
    # NATIONS = [[50,30],[20,40]]
    # solution()
    # N = 2
    # L = 40
    # R = 50
    # UNIONS = []
    # USED_NATIONS = [[False for _ in range(N)] for _ in range(N)]
    # NATIONS = [[50,30],[20,40]]
    # solution()
    # N = 2
    # L = 20
    # R = 50
    # UNIONS = []
    # USED_NATIONS = [[False for _ in range(N)] for _ in range(N)]
    # NATIONS = [[50,30],[30,40]]
    # solution()
    # N = 3
    # L = 5
    # R = 10
    # UNIONS = []
    # USED_NATIONS = [[False for _ in range(N)] for _ in range(N)]
    # NATIONS = [[10,15,20],[20,30,25],[40,22,10]]
    # solution()
    N = 4
    L = 10
    R = 50
    UNIONS = []
    USED_NATIONS = [[False for _ in range(N)] for _ in range(N)]
    NATIONS = [[10,100,20,90],[80,100,60,70],[70,20,30,40],[50,20,100,10]]
    solution()
