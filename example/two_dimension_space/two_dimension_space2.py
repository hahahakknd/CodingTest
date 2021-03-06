def solution(size: int) -> None:
    space: list = [[0 for _ in range(0, size)] for _ in range(0, size)]
    position: list = [0,0]
    order: int = 1
    directions: list = [[0,1], [1,0], [0,-1], [-1,0]]  # 오른쪽, 아래, 왼쪽, 위
    direction: list = directions[0]
    next_direction = lambda index:directions[(index+1)%4]

    while order <= size*size:
        space[position[0]][position[1]] = order
        order += 1

        # 다음 포지션 계산
        next_position = [position[i]+v for i, v in enumerate(direction)]

        # 포지션의 유효성 검사
        if next_position[0] < 0 or next_position[1] < 0                  \
                or next_position[0] >= size or next_position[1] >= size  \
                or space[next_position[0]][next_position[1]] != 0:       \
            # 유효하지 않는 케이스, 다음 방향을 구한다.
            direction = next_direction(directions.index(direction))
            # 다음 포지션 계산
            next_position = [position[i]+v for i, v in enumerate(direction)]

        # 유효한 케이스, 포지션을 결정한다.
        position = next_position

    # 이차원 공간 출력
    for row in space:
        print(row)
    return

# Input 오류는 고려하지 않는다.
if __name__ == '__main__':
    solution(int(input()))
