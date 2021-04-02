def solution(max_num, find_num) -> None:
    count = 0
    for i in range(1, max_num+1):
        for j in str(i):
            if int(j) == find_num:
                count += 1
    print(count)
    return

# Input 오류는 고려하지 않는다.
if __name__ == '__main__':
    inputs = input().split(" ")
    solution(int(inputs[0]), int(inputs[1]))
    # solution(11, 1)
    # solution(100, 3)
