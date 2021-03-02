def solution(schedule: list) -> None:
    return

# Input 오류는 고려하지 않는다.
if __name__ == '__main__':
    input_schedule: list = []
    loop_count: int = int(input())
    for _ in range(0, loop_count):
        input_schedule.append([int(x) for x in input().split(' ')])
    solution(input_schedule)
