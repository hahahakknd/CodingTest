import sys

def make_max_list(sequence: list, caches: list) -> list:
    max_list: list = [sequence[0]]
    max_value: int = sequence[0]

    tmp_list: list = []
    for cache in caches:
        if max_value < cache[0]:
            if len(tmp_list) < len(cache):
                tmp_list = cache
                continue

    if tmp_list != 0:
        return max_list + tmp_list

    for value in sequence[1:]:
        if max_value >= value:
            continue
        max_list.append(value)
        max_value = value

    return max_list

def solution(num_seq: list) -> None:
    caches: list = [[] for _ in num_seq]
    answer: list = []

    caches[len(caches)-1] = [num_seq[len(num_seq)-1]]
    answer = caches[len(caches)-1]

    for i in range(len(num_seq)-2, -1, -1):
        caches[i] = make_max_list(num_seq[i:], caches[i+1:])
        if len(answer) < len(caches[i]):
            answer = caches[i]

    print(len(answer))
    return

# Input 오류는 고려하지 않는다.
if __name__ == '__main__':
    input()  # 수열 크기는 버린다.
    num_sequence: list = [int(number) for number in input().split(' ')]
    solution(num_sequence)
