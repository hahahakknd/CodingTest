def min_index(args):
    return min(range(len(args)), key=args.__getitem__)

def find_short_cost(oil_bank_list) -> int:
    global distance

    cost = 0
    print("oil_bank_list", oil_bank_list)
    pos = min_index(oil_bank_list)
    print("min", pos)
    if pos != 0:
        cost += find_short_cost(oil_bank_list[:pos])
    else:
        cost += sum(distance[:pos+1]) * oil_bank_list[pos]
        print("cost", cost)
        return cost

    print("sum(distance[pos:])", sum(distance[pos:]), "oil_bank_list[pos]", oil_bank_list[pos])
    cost += sum(distance[pos:]) * oil_bank_list[pos]
    print("cost", cost)
    return cost

# 왼쪽에 가까운 최소값을 찾아서 남은 거리만큼의 기름을 다 채우고 가면 된다.
# 재귀로 풀면 될 듯...
# 왼쪽에 가장 가까운 최소값을 찾는 방법은??? -> 그냥 min 함수로???
def solution(oil_bank_list) -> None:
    print(find_short_cost(oil_bank_list[0:len(oil_bank_list)-1]))
    return

# Input 오류는 고려하지 않는다.
if __name__ == '__main__':
    # input()
    # distance = [int(x) for x in input().split(" ")]
    # oil_bank = [int(x) for x in input().split(" ")]
    # solution(oil_bank)
    # distance = [2,3,1]
    # oil_bank = [5,2,4,1]
    # solution(oil_bank)
    distance = [3,3,4]
    oil_bank = [1,1,1,1]
    solution(oil_bank)
