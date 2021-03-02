import sys

def solution(size: int) -> None:
    space: list = [0 for _ in range(0, size*size)]
    postion: int = 0
    order: int = 1
    directions: list = [1, size, -1, -size]  # 오른쪽, 아래, 왼쪽, 위
    direction: int = directions[0]
    next_direction = lambda index:directions[(index+1)%4]

    for _ in range(0, size*size):
        space[postion] = order
        order += 1
        if direction == directions[0]:    # 오른쪽
            if (postion+1)%size == 0 or space[postion+direction] != 0:
                direction = next_direction(directions.index(direction))
        elif direction == directions[1]:  # 아래
            if postion+direction > len(space) or space[postion+direction] != 0:
                direction = next_direction(directions.index(direction))
        elif direction == directions[2]:  # 왼쪽
            if postion%size == 0 or space[postion+direction] != 0:
                direction = next_direction(directions.index(direction))
        elif direction == directions[3]:  # 위
            if postion+direction < 0 or space[postion+direction] != 0:
                direction = next_direction(directions.index(direction))

        postion += direction

    # 이차원 공간 출력
    start_pos: int = 0
    for _ in range(0, size):
        print(space[start_pos:start_pos+size])
        start_pos += size
    return

# Input 오류는 고려하지 않는다.
if __name__ == '__main__':
    solution(int(input()))
