seats = []

def find_short_distance(people_count, pos) -> int:
    if people_count == 2:
        return int(seats[len(seats)-1]) - int(seats[pos])

    # 항상 3 이상
    if people_count == len(seats)-pos:
        distance = int(seats[pos+1]) - int(seats[pos])
        prev_dist = int(seats[pos+1])
        for i in range(pos+2,len(seats)):
            tmp_distance = int(seats[i]) - prev_dist
            if distance > tmp_distance:
                distance = tmp_distance
            prev_dist = int(seats[i])
        return distance

    short_distance = -1
    for i in range(pos, len(seats)):
        if people_count == len(seats)-i:
            tmp_distance = find_short_distance(people_count, i)
            if short_distance < tmp_distance:
                short_distance = tmp_distance
            break
        for j in range(i+1, len(seats)):
            tmp_short_distance = 0
            tmp_distance_1 = int(seats[j]) - int(seats[i])
            tmp_distance_2 = find_short_distance(people_count-1, j)
            if tmp_distance_1 < tmp_distance_2:
                tmp_short_distance = tmp_distance_1
            else:
                tmp_short_distance = tmp_distance_2
            if short_distance < tmp_short_distance:
                short_distance = tmp_short_distance
    return short_distance

def solution(people_count) -> None:
    print(find_short_distance(people_count, 0))
    return

# Input 오류는 고려하지 않는다.
if __name__ == '__main__':
    # for _ in range(int(input())):
    #     seats = input().split(' ')
    #     seats.sort()
    #     solution(int(input().split(' ')[1]))
    seats = ['10','100','200']
    solution(3)
    seats = ['11','17','19','21','22','23','28']
    solution(3)
    seats = ['11','19','24','26','29','30']
    solution(4)
    seats = ['11','19','20','21','22','23']
    solution(3)
