import sys

def print_space(space: list) -> None:
    for row in space:
        print(row)
    return

def solution(size: int) -> None:
    space: list = [[0 for _ in range(0, size)] for _ in range(0, size)]
    row: int = 0
    column: int = 0
    order: int = 1      # 탐색 순서
    direction: int = 1  # 탐색 방향
    is_column_changed: bool = True
    is_direction_changed: bool = False

    for i in range(0, size*size):
        space[row][column] = order
        order += 1

        if is_column_changed == True:
            if column+direction == -1 or column+direction == size or space[row][column+direction] != 0:
                is_direction_changed = True
        else:
            if row+direction == -1 or row+direction == size or space[row+direction][column] != 0:
                is_direction_changed = True

        if is_direction_changed == True:
            if row == 0 and column == size-1:  # 아래로 방향전환, Row 가 바뀜
                direction = 1
                is_column_changed = False
                is_direction_changed = False
            elif row == size-1 and column == size-1:  # 왼쪽으로 방향전환, Column 이 바뀜
                direction = -1
                is_column_changed = True
                is_direction_changed = False
            elif row == size-1 and column == 0:  # 위로 방향전환, Row 가 바뀜
                direction = -1
                is_column_changed = False
                is_direction_changed = False
            elif row == 0 and column == 0:  # 오른쪽으로 방향전환, Column 이 바뀜
                direction = 1
                is_column_changed = True
                is_direction_changed = False

        if is_column_changed == True:
            column += direction
        else:
            row += direction

    print_space(space)
    return

# Input 오류는 고려하지 않는다.
if __name__ == '__main__':
    solution(int(input()))
