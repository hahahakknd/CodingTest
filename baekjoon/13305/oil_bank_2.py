# 장원형 풀이는 첫번째 주유소부터 시작하여 작은 값이 나올때가지 그냥 쭉 반복한다.
# 나는 최소값을 찾는 이유 때문에 항상 O(n) 만큼의 시간복잡도가 추가된다.
# 답을 찾는 논리는 같은데, 풀이법의 차이 때문에 시간초과가 발생한다.
def solution() -> None:
    global DISTANCES, OIL_BANKS
    cost = 0
    dist_sum = DISTANCES[0]
    cur_cost = OIL_BANKS[0]
    for i in range(1,len(OIL_BANKS)):
        if cur_cost > OIL_BANKS[i]:
            cost += cur_cost * dist_sum
            cur_cost = OIL_BANKS[i]
            dist_sum = DISTANCES[i]
        else:
            dist_sum += DISTANCES[i]
    cost += cur_cost * dist_sum
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
