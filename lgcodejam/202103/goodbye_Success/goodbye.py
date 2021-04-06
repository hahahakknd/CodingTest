import bisect

input_nums = []
base_nums = [202021, 20202021,
             202002021, 202012021, 202022021, 202032021, 202042021,
             202052021, 202062021, 202072021, 202082021, 202092021]

# BinarySearch 를 써도 Python 에서는 시간초과가 발생한다.
# def find_hello_num(org_num, find_start_pos) -> int:
#     global input_nums
#     count = 0
#     for base_num in base_nums:
#         search_num = base_num - org_num
#         found_pos = bisect.bisect_left(input_nums, search_num, lo=find_start_pos)
#         if found_pos < len(input_nums) and input_nums[found_pos] == search_num:
#             for i in range(found_pos, len(input_nums)):
#                 if input_nums[i] != search_num:
#                     break
#                 count += 1
#     return count

def make_num_dict() -> dict:
    global input_nums
    num_dict = {}
    for i, value_str in enumerate(input_nums):
        value_int = int(value_str)
        if num_dict.get(value_int) == None:
            num_dict[value_int] = 0
        num_dict[value_int] += 1
    return num_dict

# 조합을 사용한다. nCr
# 정확히는 아래와 같은 로직을 따른다.
# 1. 중복되는 값은 카운팅하며 리스트를 정리한다. O(n)
# 2. 리스트를 돌며 Goodbye 값이 되는 12가지 케이스에 대해서 값들을 검사한다. O(n)
# 3. Goodbye 값에서 리스트의 값을 빼서 찾을 숫자를 만든다.
# 4. 찾는 숫자가 현재 선택된 리스트의 값과 같으면 nC2 의 조합만큼 쌍이 생긴다.
# 5. 찾는 숫자가 현재 선택된 리스트의 값과 다르면 찾는 숫자가 리스트에 있는지 찾는다.
# 6. 있으면 찾는 숫자의 갯수와 찾은 숫자의 갯수를 곱한다.
# 7. 마지막 카운팅에서 2로 나누어 준다.
#
# 4번에서 nC2 는 n(n-1)/2 이다.
# 6번에서 갯수를 구하기 위해 두 수의 갯수를 곱해준다.
# 하지만 5번에서 숫자를 찾는 범위가 전체리스트이기 때문에 항상 중복되어 찾아진다.
# 따라서 중복된 갯수를 빼줘야 하는데, Python 의 Dict 에서는 찾는 범위를 조정할 수 없다.
# 그래서 조합을 구할 때 2로 나누는 과정을 생략하고, 전체범의에서 찾을 때 중복되게 찾게하고, 마지막에 2로 나누어준다.
# 6번과정에서 2로 나누면 홀수인 경우에 나머지가 생겨 올바른 답을 찾을 수 없다.

def solution() -> None:
    num_dict = make_num_dict()
    count = 0
    for key, value in num_dict.items():
        for base_num in base_nums:
            search_num = base_num - key
            if search_num == key:
                count += value*(value-1)
            elif search_num in num_dict:
                count += value*num_dict[search_num]
    print(count//2)
    return

# Input 오류는 고려하지 않는다.
if __name__ == '__main__':
    for _ in range(int(input())):
        input()
        input_nums = input().split(' ')
        # 정렬이 들어가도 400ms 차이밖에 안난다.
        # BinarySeach 사용 시에 시간초과가 났던 것은 알고리즘 문제였다. ㅠㅠ
        # input_nums.sort()
        solution()
    # input_nums = ['101010','101010','101011','101011']
    # solution()
    # input_nums = ['100000','100000','100000','101011','101011']
    # solution()
    # input_nums = ['202021','0','1','202020']
    # solution()
