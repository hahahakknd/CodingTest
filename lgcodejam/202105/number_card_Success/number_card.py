import sys

def solution() -> None:
    global DATAS
    for data in DATAS:
        left_numbers = []
        right_numbers = []
        is_left = True
        for num in data:
            if is_left:
                left_numbers.append(num)
                is_left = False
            else:
                right_numbers.insert(0, num)
                is_left = True
        for num in left_numbers + right_numbers:
            print(num, end=' ')
        print('')
    return

# Input 오류는 고려하지 않는다.
if __name__ == '__main__':
    DATAS = []
    loop_count = int(sys.stdin.readline().rstrip())
    for i in range(loop_count):
        input_data = sys.stdin.readline().rstrip().split(' ')
        card_dec = []
        for j in range(len(input_data)):
            number = j+1
            num_loop_count = int(input_data[j])
            if num_loop_count == 0:
                continue
            for _ in range(num_loop_count):
                if number == 6:
                    card_dec.append(9)
                else:
                    card_dec.append(number)
        card_dec.sort(reverse=True)
        DATAS.append(card_dec)
    solution()


    # a = [["0", "0", "0", "0", "0", "2", "1", "1", "1"],
    #      ["1", "1", "1", "1", "1", "1", "1", "1", "1"],
    #      ["1", "1", "3", "0", "0", "0", "0", "0", "0"],
    #      ["1", "2", "2", "0", "0", "0", "0", "0", "0"],
    #      ["2", "2", "2", "2", "2", "2", "2", "2", "2"]]
    # for i in range(len(a)):
    #     input_data = a[i]
    #     card_dec = []
    #     for j in range(len(input_data)):
    #         number = j+1
    #         num_loop_count = int(input_data[j])
    #         if num_loop_count == 0:
    #             continue
    #         for _ in range(num_loop_count):
    #             if number == 6:
    #                 card_dec.append(9)
    #             else:
    #                 card_dec.append(number)
    #     card_dec.sort(reverse=True)
    #     DATAS.append(card_dec)
    # solution()
