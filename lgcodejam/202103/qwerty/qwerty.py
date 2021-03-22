keyboard = [['Q','W','E','R','T','Y','U','I','O','P'],
            ['A','S','D','F','G','H','J','K','L'],
            ['Z','X','C','V','B','N','M']]

def find_position(alphabet):
    for row in range(3):
        try:
            column = keyboard[row].index(alphabet)
            return row, column
        except ValueError:
            pass

def solution(word) -> None:
    time = 1
    cur_position = find_position(word[0])
    for word_pos in range(1,len(word)):
        next_position = find_position(word[word_pos])
        row_step = next_position[0] - cur_position[0]
        column_step = next_position[1] - cur_position[1]
        if row_step == -1 and column_step < 0:
            time += 2
        elif row_step == -2 and column_step < 0:
            if column_step == -1:
                time += 2
            else:
                time += 4
        elif row_step == 1 and column_step > 0:
            time += 2
        elif row_step == 2 and column_step > 0:
            if column_step == 1:
                time += 2
            else:
                time += 4
        if row_step < 0:
            row_step = -row_step
        if column_step < 0:
            column_step = -column_step
        if row_step == 1:
            if column_step <= 1:
                column_step = 0
            else:
                column_step -= 1
            time += 2
        elif row_step == 2:
            if column_step <= 2:
                column_step = 0
            else:
                column_step -= 2
            time += 4
        time += (column_step*2 + 1)
        cur_position = next_position

    print(time)
    return

# Input 오류는 고려하지 않는다.
if __name__ == '__main__':
    loop_count = int(input())
    for _ in range(loop_count):
        solution(input())
    # solution('QWERTY')
    # solution('LOM')
    # solution('FFGGFF')
    # solution('VGTRDCF')
    # solution('MPML')
    # solution('XQ')
