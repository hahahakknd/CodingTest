def make_stack(postion, x_end, y_end) -> None:
    global BANNER, STACK
    directions = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]
    for direction in directions:
        x = postion[0] + direction[0]
        y = postion[1] + direction[1]
        if x in range(0, x_end) and y in range(0, y_end) and BANNER[x][y] == 1:
            STACK.append([x,y])
            BANNER[x][y] = 0

def find_number(x_end, y_end) -> None:
    global BANNER, STACK
    for x in range(x_end):
        for y in range(y_end):
            if BANNER[x][y] == 1:
                make_stack([x,y], x_end, y_end)
                STACK.append([x,y])
                BANNER[x][y] = 0
                return

def solution(x_end, y_end) -> None:
    global BANNER, STACK
    count = 0
    while True:
        find_number(x_end, y_end)
        if len(STACK) == 0:
            print(count)
            return
        while len(STACK) != 0:
            postion = STACK.pop()
            make_stack(postion, x_end, y_end)
        count += 1

# Input 오류는 고려하지 않는다.
if __name__ == '__main__':
    input_data = input().split(" ")
    BANNER = []
    STACK = []
    for _ in range(int(input_data[0])):
        BANNER.append([int(x) for x in input().split(" ")])
    solution(int(input_data[0]), int(input_data[1]))
    # BANNER = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    #           [0,0,0,1,0,0,0,1,0,0,0,1,0,1,1,1,1,1,0],
    #           [0,0,1,0,1,0,0,1,1,0,0,1,0,0,0,1,0,0,0],
    #           [0,1,0,0,0,1,0,1,0,1,0,1,0,0,0,1,0,0,0],
    #           [0,1,1,1,1,1,0,1,0,1,0,1,0,0,0,1,0,0,0],
    #           [0,1,0,0,0,1,0,1,0,0,1,1,0,0,0,1,0,0,0],
    #           [0,1,0,0,0,1,0,1,0,0,0,1,0,0,0,1,0,0,0],
    #           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    #           [0,1,1,1,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0],
    #           [1,0,0,0,1,0,1,0,0,0,1,0,0,0,0,0,0,0,0],
    #           [1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0],
    #           [1,0,0,0,1,0,1,0,0,0,1,0,0,0,0,0,0,0,0],
    #           [0,1,1,1,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0]]
    # STACK = []
    # solution(13,19)
    # BANNER = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    #           [0,0,0,1,0,0,0,1,0,0,0,1,0,1,1,1,1,1,0],
    #           [0,0,1,0,1,0,0,1,1,0,0,1,0,0,0,1,0,0,0],
    #           [0,1,0,0,0,1,0,1,0,1,0,1,0,0,0,1,0,0,0],
    #           [0,1,1,1,1,1,0,1,0,1,0,1,0,0,0,1,0,0,0],
    #           [0,1,0,0,0,1,0,1,0,0,1,1,0,0,0,1,0,0,0],
    #           [0,1,0,0,0,1,0,1,0,0,0,1,0,0,0,1,0,0,0],
    #           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
    # STACK = []
    # solution(8,19)
    # BANNER = [[0,0,0],
    #           [0,1,0]]
    # STACK = []
    # solution(2,3)
