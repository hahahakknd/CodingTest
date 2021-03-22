def check_hello(first_num:str, second_num:str) -> bool:
    is_first_num_minus = (first_num[0] == '-')
    first_num_length = len(first_num) if is_first_num_minus == False else len(first_num)-1
    is_second_num_minus = (second_num[0] == '-')
    second_num_length = len(second_num) if is_second_num_minus == False else len(second_num)-1

    # 둘 다 음수
    if is_first_num_minus is True and is_second_num_minus is True:
        return False

    # 첫번째 숫자가 음수
    if is_first_num_minus is True and is_second_num_minus is False:
        if first_num_length > second_num_length:
            return False
        if first_num_length == second_num_length:
            for i, second_num_digit in enumerate(second_num):
                if first_num[i+1] > second_num_digit:
                    return False

    # 두번째 숫자가 음수
    if is_first_num_minus is False and is_second_num_minus is True:
        if first_num_length > second_num_length:
            return False
        if first_num_length == second_num_length:
            for i, first_num_digit in enumerate(first_num):
                if second_num[i+1] > first_num_digit:
                    return False

    # 두 수를 더했을 때 양수가 나옴
    # 두 수 모두 길이가 6보다 작다.
    if first_num_length < 6 and second_num_length < 6:
        sum_number = int(first_num) + int(second_num)
        sum_number_str = str(sum_number)
        if len(sum_number_str) < 6:
            return False
        if sum_number_str[0:4] != '2020' or sum_number_str[len(sum_number_str)-4:len(sum_number_str)] != '2021':
            return False
        return True



    if len(first_num) < 5:
        first_number_end = first_num[]

    return True

def solution(numbers:list) -> None:
    count = 0
    numbers_size = len(numbers)
    for i in range(numbers_size):
        if (i+2) == numbers_size:
            if check_hello(numbers[i], numbers[i+1]) is True:
                count += 1
                break
        for j in range(i+1, numbers_size):
            if check_hello(numbers[i], numbers[j]) is True:
                count += 1
    print(count)
    return

# Input 오류는 고려하지 않는다.
if __name__ == '__main__':
    # for _ in range(int(input())):
    #     input()
    #     solution(input().split(' '))
    solution(['101010','101010','101011','101011'])
    solution(['100000','100000','100000','101011','101011'])
    solution(['202021','0','1','202020'])
