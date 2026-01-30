from math import ceil
import sys


def solution(h: int, w: int, n: int, m: int) -> None:
    vertical = ceil(h / (n + 1))
    horizon = ceil(w / (m + 1))
    print(f"{vertical * horizon}")
    return


# Input 오류는 고려하지 않는다.
if __name__ == "__main__":
    input_data = sys.stdin.readline().strip().split(" ")
    solution(
        int(input_data[0]), int(input_data[1]), int(input_data[2]), int(input_data[3])
    )
