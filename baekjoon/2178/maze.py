import sys

def find_steps() -> None:
    global DIRECTIONS, CHECK_MAZE, MAZE, END_SIZE
    stack = [[0,0]]
    while len(stack) != 0:
        point = stack.pop(0)
        for direction in DIRECTIONS:
            next_point = [point[0]+direction[0],point[1]+direction[1]]
            if     (next_point[0] == 0 and next_point[1] == 0)       \
                or next_point[0] < 0 or next_point[0] >= END_SIZE[0] \
                or next_point[1] < 0 or next_point[1] >= END_SIZE[1] \
                or MAZE[next_point[0]][next_point[1]] == 0           \
                or CHECK_MAZE[next_point[0]][next_point[1]] != 0:
                continue
            CHECK_MAZE[next_point[0]][next_point[1]] = CHECK_MAZE[point[0]][point[1]] + 1
            stack.append(next_point)
    return

def solution() -> None:
    global CHECK_MAZE, END_SIZE
    find_steps()
    print(CHECK_MAZE[END_SIZE[0]-1][END_SIZE[1]-1]+1)
    for i in CHECK_MAZE:
        print(i)
    return

# Input 오류는 고려하지 않는다.
if __name__ == '__main__':
    DIRECTIONS = [[1,0],[0,1],[-1,0],[1,0]]
    # input_data = sys.stdin.readline().rstrip().split(' ')
    # END_SIZE = [int(input_data[0]),int(input_data[1])]
    # CHECK_MAZE = [[0 for _ in range(END_SIZE[1])] for _ in range(END_SIZE[0])]
    # MAZE = []
    # for _ in range(END_SIZE[0]):
    #     MAZE.append([int(x) for x in sys.stdin.readline().rstrip()])
    # solution()
    END_SIZE = [4,6]
    CHECK_MAZE = [[0 for _ in range(END_SIZE[1])] for _ in range(END_SIZE[0])]
    MAZE = [[1,0,1,1,1,1],
            [1,0,1,0,1,0],
            [1,0,1,0,1,1],
            [1,1,1,0,1,1]]
    solution()
    END_SIZE = [4,6]
    CHECK_MAZE = [[0 for _ in range(END_SIZE[1])] for _ in range(END_SIZE[0])]
    MAZE = [[1,1,0,1,1,0],
            [1,1,0,1,1,0],
            [1,1,1,1,1,1],
            [1,1,1,1,0,1]]
    solution()
    END_SIZE = [2,25]
    CHECK_MAZE = [[0 for _ in range(END_SIZE[1])] for _ in range(END_SIZE[0])]
    MAZE = [[1,0,1,1,1,0,1,1,1,0,1,1,1,0,1,1,1,0,1,1,1,0,1,1,1],
            [1,1,1,0,1,1,1,0,1,1,1,0,1,1,1,0,1,1,1,0,1,1,1,0,1]]
    solution()
    END_SIZE = [7,7]
    CHECK_MAZE = [[0 for _ in range(END_SIZE[1])] for _ in range(END_SIZE[0])]
    MAZE = [[1,0,1,1,1,1,1],
            [1,1,1,0,0,0,1],
            [1,0,0,0,0,0,1],
            [1,0,0,0,0,0,1],
            [1,0,0,0,0,0,1],
            [1,0,0,0,0,0,1],
            [1,1,1,1,1,1,1]]
    solution()
    END_SIZE = [6,47]
    CHECK_MAZE = [[0 for _ in range(END_SIZE[1])] for _ in range(END_SIZE[0])]
    MAZE = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]
    solution() # 52
