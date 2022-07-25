import sys

def move(num: int, from_pos: int, to_pos: int, aux_pos: int) -> None:
    if num == 1:
        print(from_pos, to_pos)
        return

    # num-1개의 원판을 from_pos 에서 aux_pos 로 옮기는데 to_pos 를 보조 위치로 사용한다.
    move(num-1, from_pos, aux_pos, to_pos)

    # 1개의 원판을 from_pos 에서 to_pos 로 옮기는데 aux_pos 를 보조 위치로 사용한다.
    move(1, from_pos, to_pos, aux_pos)

    # num-1개의 원판을 aux_pos 에서 to_pos 로 옮기는데 from_pos 를 보조 위치로 사용한다.
    move(num-1, aux_pos, to_pos, from_pos)

def hanoi(n: int) -> None:
    print(2**n-1)
    move(n, 1, 3, 2) # n개의 원판을 1번 위치에서 3번 위치로 옮기는데 2번 위치를 보조 위치로 사용한다.

def solution(n: int) -> None:
    hanoi(n)

# Input 오류는 고려하지 않는다.
if __name__ == '__main__':
    input_data = sys.stdin.readline().rstrip().split(' ')
    solution(int(input_data[0]))
