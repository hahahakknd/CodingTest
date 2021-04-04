def make_str(seq_num) -> str:
    result = str(seq_num[0])
    for x in range(1,len(seq_num)):
        result += " " + str(seq_num[x])
    return result

def solution(seq_num:list, n, m) -> None:
    for j in range(1,10):
        if j > n:
            break
        if m == 1:
            seq_num.append(j)
            print(make_str(seq_num))
        else:
            seq_num.append(j)
            solution(seq_num, n, m-1)
        seq_num.pop()
    return

# Input 오류는 고려하지 않는다.
if __name__ == '__main__':
    input_data = input().split(" ")
    solution([], int(input_data[0]), int(input_data[1]))
    # solution([], 3, 1)
    # solution([], 4, 2)
    # solution([], 3, 3)
