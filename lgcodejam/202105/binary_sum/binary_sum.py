import sys

def make_bin_to_dec(bin_num) -> int:
    dec_number = 0
    count = len(bin_num)-1
    for i in bin_num:
        dec_number += i*(2**count)
        count -= 1
    return dec_number

def make_dec_to_bin(dec_num) -> list:
    bin_number = []
    tmp_number = dec_num
    div_rst = divmod(tmp_number, 2)
    while True:
        bin_number.insert(0, div_rst[1])
        if div_rst[0] <= 1:
            bin_number.insert(0, div_rst[0])
            break
        tmp_number = div_rst[0]
        div_rst = divmod(tmp_number, 2)
    return bin_number

def solution() -> None:
    global X_DATA, BIN_DATA
    for i in range(len(X_DATA)):
        match_rst = 0
        anw = X_DATA[i]
        bin_list = BIN_DATA[i]
        for i in range(len(bin_list)-1):
            for j in range(i+1, len(bin_list)):
                bin_rst = []
                if len(bin_list[i]) >= len(bin_list[j]):
                    count = len(bin_list[j])-1
                    for k in range(len(bin_list[i])-1, -1, -1):
                        if count >= 0:
                            sum_rst = bin_list[i][k] + bin_list[j][count]
                            if sum_rst > 1:
                                bin_rst.insert(0, 0)
                            else:
                                bin_rst.insert(0, sum_rst)
                            count -= 1
                        else:
                            bin_rst.insert(0, bin_list[i][k])
                else:
                    count = len(bin_list[i])-1
                    for k in range(len(bin_list[j])-1, -1, -1):
                        if count >= 0:
                            sum_rst = bin_list[j][k] + bin_list[i][count]
                            if sum_rst > 1:
                                bin_rst.insert(0, 0)
                            else:
                                bin_rst.insert(0, sum_rst)
                            count -= 1
                        else:
                            bin_rst.insert(0, bin_list[j][k])
                if anw == make_bin_to_dec(bin_rst):
                    match_rst += 1
        print(match_rst)
    return

# Input 오류는 고려하지 않는다.
if __name__ == '__main__':
    X_DATA = []
    BIN_DATA = []
    # loop_count = int(sys.stdin.readline().rstrip())
    # for _ in range(loop_count):
    #     X_DATA.append(int(sys.stdin.readline().rstrip().split(' ')[1]))
    #     bin_set = [make_dec_to_bin(int(x)) for x in sys.stdin.readline().rstrip().split(' ')]
    #     BIN_DATA.append(bin_set)
    # solution()

    a = ['0', '1', '4']
    b = [['2', '2', '3', '3'],
         ['2', '3', '3', '2'],
         ['3', '7', '5', '6']]
    for r in range(len(a)):
        X_DATA.append(int(a[r]))
        bin_set = [make_dec_to_bin(int(x)) for x in b[r]]
        BIN_DATA.append(bin_set)
    solution()
