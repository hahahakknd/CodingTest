import sys

def solution(up_length: int, down_length: int, total_length: int) -> None:
    remain_length: int = total_length - up_length  # 항상 0 보다 크다.

    if remain_length == 0:
        print(1)
        return

    distance_for_day: int = up_length - down_length
    if remain_length % distance_for_day == 0:
        print((remain_length // distance_for_day) + 1)  # 마지막 남는 길이에 밤을 보내지 않아도 되니까 '+1' 한다.
    else:
        print((remain_length // distance_for_day) + 2)  # 마지막 남는 길이에 밤을 보내야 되니까 '+2' 한다.
    return

# Input 오류는 고려하지 않는다.
if __name__ == '__main__':
    input_data = sys.stdin.readline().rstrip().split(' ')
    solution(int(input_data[0]), int(input_data[1]), int(input_data[2]))
