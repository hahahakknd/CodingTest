import sys

# 이 문제는 중복을 허용하지 않고 순서없이 뽑는 경우의 수인 "조합" 에 관한 문제이다.
def count_bridge(west_city_num: int, east_city_num: int) -> int:
    # 아래 두 If 문은 없어도 되지만 불필요한 연산을 없애기 위해 남겨둔다.
    if west_city_num == 1:    # 서쪽 도시가 1개이면
        return east_city_num  # 동쪽 도시 갯수만큼 다리를 연결할 수 있다.

    if west_city_num == east_city_num:  # 서쪽 도시와 동쪽 도시 갯수가 같으면
        return 1                        # 1번만 도시를 연결할 수 있다.

    # 분자를 구한다.
    numerator: int = 1
    for i in range(0, west_city_num):
        multipled_number: int = east_city_num - i
        if multipled_number == 1:
            break
        numerator = numerator * multipled_number

    # 분모를 구한다.
    denominator: int = 1
    for i in range(0, west_city_num):
        multipled_number: int = west_city_num - i
        if multipled_number == 1:
            break
        denominator = denominator * multipled_number

    return numerator // denominator

if __name__ == '__main__':
    loop_count: int = int(input())
    for num in range(0, loop_count):
        city_list: list = input().split(' ')
        print(count_bridge(int(city_list[0]), int(city_list[1])))

##
## 아래 코드는 답은 맞는데 시간이 초과되는 코드이다.
##
# def count_bridge(west_city_num: int, east_city_num: int) -> int:
#     if west_city_num == 1:    # 서쪽 도시가 1개이면
#         return east_city_num  # 동쪽 도시 갯수만큼 다리를 연결할 수 있다.

#     if west_city_num == east_city_num:  # 서쪽 도시와 동쪽 도시 갯수가 같으면
#         return 1                        # 1번만 도시를 연결할 수 있다.

#     sub_birdge_num: int = count_bridge(west_city_num-1, east_city_num-1)
#     before_birdge_num: int = count_bridge(west_city_num, east_city_num-1)

#     return sub_birdge_num + before_birdge_num

# if __name__ == '__main__':
#     loop_count: int = int(input())
#     for i in range(0, loop_count):
#         city_list: list = input().split(' ')
#         print(count_bridge(int(city_list[0]), int(city_list[1])))
