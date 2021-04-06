def calculate(left_number:list, right_number:list, remain_numnber:list):
    remain_numnber_size = len(remain_numnber)
    if remain_numnber_size == 0:
        return int(''.join(left_number))*int(''.join(right_number))

    if remain_numnber_size == 1:
        tmp_number = left_number + remain_numnber[0:1]
        first_num = calculate(tmp_number, right_number, [])
        tmp_number = right_number + remain_numnber[0:1]
        second_num = calculate(left_number, tmp_number, [])
        if first_num > second_num:
            return first_num
        return second_num

    tmp_number_1 = left_number + remain_numnber[0:1]
    tmp_number_2 = right_number + remain_numnber[1:2]
    first_num = calculate(tmp_number_1, tmp_number_2, remain_numnber[2:remain_numnber_size])

    tmp_number_1 = left_number + remain_numnber[1:2]
    tmp_number_2 = right_number + remain_numnber[0:1]
    second_num = calculate(tmp_number_1, tmp_number_2, remain_numnber[2:remain_numnber_size])

    if first_num > second_num:
        return first_num
    return second_num

def solution(cards:list) -> None:
    num_pos = len(cards)
    for i in range(num_pos):
        if cards[i] == '6':
            cards[i] = '9'
    cards.sort(reverse=True)

    left_number = [cards[0]]
    right_number = [cards[1]]
    print(calculate(left_number, right_number, cards[2:num_pos]))
    return

# Input 오류는 고려하지 않는다.
if __name__ == '__main__':
    loop_count = int(input())
    for _ in range(loop_count):
        solution(list(input()))
    # solution(list('90000'))
    # solution(list('66'))
    # solution(list('102030'))
    # solution(list('20202021'))
    # solution(list('999999999999999999'))
