def dfs(value_list:list, index, sum) -> None:
    if index == len(value_list):
        if sum != 0:  # input 값이 0 보다 크기때문에
            result_data.add(sum)
        return
    dfs(value_list, index+1, sum)
    dfs(value_list, index+1, sum+value_list[index])

def solution() -> None:
    dfs(input_data, 0, 0)
    num = 0
    for data in sorted(result_data):
        num += 1
        if num != data:
            print(num)
            return
    print(num+1)
    return

# Input 오류는 고려하지 않는다.
if __name__ == '__main__':
    input()
    result_data = set()  # Set 은 Unordered 이다.
    input_data = [int(x) for x in input().split(" ")]
    solution()
    # result_data = set()
    # input_data = [5,1,2]
    # solution()
    # print(input_data)
    # print(result_data)
    # result_data.clear()
    # input_data = [2,1,4]
    # solution()
    # print(input_data)
    # print(result_data)
    # result_data.clear()
    # input_data = [2,1,2,7]
    # solution()
    # print(input_data)
    # print(result_data)
    # result_data.clear()
    # input_data = [3,1,1,3]
    # solution()
    # print(input_data)
    # print(result_data)
