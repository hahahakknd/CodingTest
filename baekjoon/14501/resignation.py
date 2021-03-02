import sys

def max_earn(schedule: list) -> int:
    max_money: int = 0
    for index, work in enumerate(schedule):
        days: int = work[0]
        if index+days > len(schedule):
            continue
        money: int = max_earn(schedule[index+days:])
        if max_money < money+work[1]:
            max_money = money+work[1]
    return max_money

def solution(schedule: list) -> None:
    print(max_earn(schedule))
    return

# Input 오류는 고려하지 않는다.
if __name__ == '__main__':
    input_schedule: list = []
    loop_count: int = int(input())
    for _ in range(0, loop_count):
        input_schedule.append([int(x) for x in input().split(' ')])
    solution(input_schedule)
