import sys

WIN = 3
DRAW = 1
LOSE = 0

def match(match_count, match_data) -> None:
    global DATAS, RESULTS
    first_nation = DATAS[match_count][0]
    second_nation = DATAS[match_count][1]
    # Win
    if DATAS[match_count][2] != 0.0:
        match_result = match_data.copy()
        match_result[first_nation] += WIN
        match_result[second_nation] += LOSE
        if match_count == 5:
            RESULTS.append(match_result)
        else:
            match(match_count+1, match_result)
    # Draw
    if DATAS[match_count][3] != 0.0:
        match_result = match_data.copy()
        match_result[first_nation] += DRAW
        match_result[second_nation] += DRAW
        if match_count == 5:
            RESULTS.append(match_result)
        else:
            match(match_count+1, match_result)
    # Lose
    if DATAS[match_count][4] != 0.0:
        match_result = match_data.copy()
        match_result[first_nation] += LOSE
        match_result[second_nation] += WIN
        if match_count == 5:
            RESULTS.append(match_result)
        else:
            match(match_count+1, match_result)
    return

def solution() -> None:
    global DATAS, RESULTS, NEXT_PROBABLITY
    match_result = {}
    for key in NEXT_PROBABLITY:
        match_result[key] = 0
    match(0, match_result)
    for result in RESULTS:
        print(result)
    total_count = 0
    for result in RESULTS:
        sorted_result = sorted(result.items(), key=lambda x:x[1], reverse=True)
        first = []
        second = []
        before_score = 0
        loop_num = 0
        for rst in sorted_result:
            if before_score != rst[1]:
                loop_num += 1
                if loop_num == 3:
                    break
                before_score = rst[1]
            if loop_num == 1:
                first.append(rst[0])
            elif loop_num == 2:
                second.append(rst[0])
        first_size = len(first)
        second_size = len(second)
        if second_size == 0:
            total_count += first_size
        else:
            total_count += (first_size * second_size)
        for nation in first:
            NEXT_PROBABLITY[nation] += 1 if second_size == 0 else second_size
        for nation in second:
            NEXT_PROBABLITY[nation] += 1 if first_size == 0 else first_size
        print("first", first)
        print("second", second)
    print("total_count", total_count)
    for key, value in NEXT_PROBABLITY.items():
        NEXT_PROBABLITY[key] = value/total_count
    for key, value in NEXT_PROBABLITY.items():
        print(format(value, "11.10f"))
    return

# Input 오류는 고려하지 않는다.
if __name__ == '__main__':
    # DATAS = []
    RESULTS = []
    NEXT_PROBABLITY = {}
    # input_data = sys.stdin.readline().rstrip().split(' ')
    # for data in input_data:
    #     NEXT_PROBABLITY[data] = 0.0
    # for _ in range(6):
    #     input_data = sys.stdin.readline().rstrip().split(' ')
    #     DATAS.append([input_data[0], input_data[1], \
    #                  float(input_data[2]), float(input_data[3]), float(input_data[4])])
    # solution()
    input_data = ['KOREA','CCC','BBB','AAA']
    for data in input_data:
        NEXT_PROBABLITY[data] = 0.0
    DATAS = [['KOREA','CCC',1.0,0.0,0.0],
             ['AAA','BBB',0.428,0.144,0.428],
             ['AAA','KOREA',0.0,0.0,1.0],
             ['CCC','BBB',0.0,0.0,1.0],
             ['KOREA','BBB',1.0,0.0,0.0],
             ['CCC','AAA',0.0,0.0,1.0]]
    solution()
