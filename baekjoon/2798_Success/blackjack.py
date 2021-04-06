import sys

def find_max_sum(card_list: list,
                 pick_count: int,
                 start_pos: int,
                 end_pos: int,
                 rest_value: int) -> int:
    if pick_count == 3:
        return -1  # 카드를 세번 다 뽑은 상태이므로 여기까지 오면 안된다.

    max_value = rest_value
    answer: int = -1
    sub_answer: int = 0

    for index in range(start_pos, end_pos):
        pick_value: int = card_list[index]
        # print('pick_card[' + str(pick_count+1) + ']: ' + str(pick_value))

        if pick_value > max_value:  # 뽑은 카드가 최대값보다 클 때
            break                   # 실패, 이 위치 다음으로는 카드를 고를필요 없다.

        if pick_value == max_value:  # 뽑은 카드가 최대값이랑 같은데
            if pick_count != 2:      # 세번째 카드를 뽑는 경우가 아니면
                break                # 실패, 이 위치 다음으로는 카드를 고를필요 없다.
            return pick_value        # 세번째 카드를 뽑는 경우이면 성공!!!

        if pick_value < max_value:   # 뽑은 카드가 최대값보다 작을 때
            if pick_count == 2:      # 세번째 카드를 뽑는 경우이면
                answer = pick_value  # 정답을 바꾸고
                continue             # 다음 정답값을 구한다.

        # 세번째 카드를 뽑는 경우가 아니면 다음 뽑기를 한다.
        sub_answer = find_max_sum(card_list, pick_count+1, index+1, end_pos, max_value-pick_value)

        # 아래에서 부분합들의 크기들을 비교하여 최대값에 가까운 값을 찾는다.

        if sub_answer == -1:  # 부분합을 구하는데 실패인 경우
            continue          # 다음 뽑기를 진행한다.

        tmp_answer: int = pick_value + sub_answer  # 뽑은 카드의 합을 구하여 정답값을 구한다.

        # 아래 케이스는 발생할 수 없다. 미리 최대값을 넘어가는 케이스를 다 걸러내기 때문이다.
        if tmp_answer > max_value:  # 정답값이 최대값보다 크면
            continue                # 다음 뽑기를 진행한다.

        if tmp_answer == max_value:  # 정답값이 최대값과 같으면
            answer = tmp_answer      # 블랙잭!!!!
            break

        if tmp_answer > answer:  # 정답값이 이전 정답값보다 크면
            answer = tmp_answer  # 정답값을 바꾸고 다음 정답값을 구한다.

    return answer

if __name__ == '__main__':
    first_input: str = input()
    split_list: list = first_input.split(' ')
    n: int = int(split_list[0])
    m: int = int(split_list[1])

    second_input: str = input()
    input_card_list: list = list(map(int, second_input.split(' ')))
    input_card_list.sort()

    print(find_max_sum(input_card_list, 0, 0, n, m))
