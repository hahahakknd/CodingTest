import sys

building_list: list = []

# 건물을 만드는데 걸리는 시간을 계산한다.
def caculateBuildTime(building_info: list) -> int:
    building_info_length = len(building_info)

    if building_info_length < 2:
        raise Exception('Invalid building information.')

    # 이미 계산되어 있다.
    if building_info[building_info_length-1] != -1:
        return building_info[building_info_length-1]

    # 계산이 안되어 있는데 선행건물이 필요없는 경우이다.
    if building_info_length == 2:
        building_info[1] = building_info[0]
        return building_info[1]

    # 계산이 안되어 있는데 선행건물이 필요한 경우이다.
    pre_build_time: int = 0
    for index in range(1, building_info_length-1):
        tmp_build_time: int = caculateBuildTime(building_list[building_info[index]-1])
        if pre_build_time < tmp_build_time:
            pre_build_time = tmp_build_time
    building_info[building_info_length-1] = pre_build_time + building_info[0]

    return building_info[building_info_length-1]

# 1번 건물이 2번을 필요로 하고 2번 건물이 1번을 필요로 하면
# 이 경우는 에러케이스로 무한루프를 돌게 된다.
# 이러한 잘못된 Input 은 없다고 가정한다.
def print_build_times():
    for building_info in iter(building_list):
        # 각 건물의 걸리는 시간을 계산한다.
        print(caculateBuildTime(building_info))

if __name__ == '__main__':
    loop_count: int = int(input())
    for num in range(0, loop_count):
        building_list.append(list(map(int, input().split(' '))))
    print_build_times()
