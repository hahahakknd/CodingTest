def min_index(length):
    global OIL_BANKS
    return min(range(length), key=OIL_BANKS.__getitem__)

def distance_sum(start, end) -> int:
    global DISTANCES
    dist_sum = 0
    for i in range(start, end):
        dist_sum += DISTANCES[i]
    return dist_sum

# 왼쪽에 가까운 최소값을 찾아서 남은 거리만큼의 기름을 다 채우고 가면 된다.
# 재귀로 풀면 될 듯...
# 왼쪽에 가장 가까운 최소값을 찾는 방법은??? -> 그냥 min 함수로???
# 시간초과가 나온다. 리스트 슬라이싱을 없애도 똑같다.
def solution() -> None:
    global DISTANCES, OIL_BANKS
    cost = 0
    length = len(OIL_BANKS)
    while True:
        pos = min_index(length)
        if pos == 0:
            cost += distance_sum(0,length) * OIL_BANKS[pos]
            break
        cost += distance_sum(pos,length) * OIL_BANKS[pos]
        length = pos
    print(cost)
    return

# Input 오류는 고려하지 않는다.
if __name__ == '__main__':
    input()
    DISTANCES = [int(x) for x in input().split(" ")]
    OIL_BANKS = [int(x) for x in input().split(" ")]
    OIL_BANKS.pop()
    solution()
    # DISTANCES = [2,3,1]
    # OIL_BANKS = [5,2,4,1]
    # OIL_BANKS.pop()
    # solution()
    # DISTANCES = [3,3,4]
    # OIL_BANKS = [1,1,1,1]
    # OIL_BANKS.pop()
    # solution()
    # DISTANCES = [1,1,1,1,1,1]
    # OIL_BANKS = [3,5,3,7,2,1,8]
    # OIL_BANKS.pop()
    # solution()
