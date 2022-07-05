import sys

def solution(total_weight: int) -> None:
    three_kg_count: int = 0
    remain_weight: int = total_weight
    total_count: int = 0

    while True:
        if remain_weight < 0:
            total_count = -1
            break

        if remain_weight%5 == 0:
            total_count = (remain_weight//5) + three_kg_count
            break

        three_kg_count += 1
        remain_weight -= 3

    print(total_count)

# Input 오류는 고려하지 않는다.
if __name__ == '__main__':
    input_data = sys.stdin.readline().rstrip().split(' ')
    solution(int(input_data[0]))
