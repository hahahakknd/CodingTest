# 끝자리 숫자가 0, 1 이거나 2의 배수만 허용된다.
def solution(start_num, end_num) -> None:
    tmp_num = end_num
    count = 1

    while True:
        if tmp_num == start_num:
            print(count)
            break

        if tmp_num < start_num:
            print(-1)
            break

        last_digit = tmp_num%10

        if last_digit != 0 and last_digit != 1 and last_digit%2 != 0:
            print(-1)
            break

        if last_digit == 1:
            tmp_num = tmp_num//10
        else:
            tmp_num = tmp_num//2

        count += 1

    return

# Input 오류는 고려하지 않는다.
if __name__ == '__main__':
    input_data = input().split(' ')
    solution(int(input_data[0]), int(input_data[1]))
    # solution(2, 162)
    # solution(4, 42)
    # solution(100, 40021)
