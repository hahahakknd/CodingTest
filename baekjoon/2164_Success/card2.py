def solution(number) -> None:
    if number == 1:
        print(1)
        return

    is_odd = (number%2 == 1)
    org_list = []
    if is_odd:
        modified_list = [x for x in range(4,number+1,2)]
        modified_list.append(2)
    else:
        modified_list = [x for x in range(2,number+1,2)]

    while True:
        if len(modified_list) == 1:
            print(modified_list[0])
            return

        is_odd = (len(modified_list)%2 == 1)
        org_list.clear()
        org_list.extend(modified_list)
        modified_list.clear()

        if is_odd:
            if len(org_list) >= 4:
                for x in range(3,len(org_list),2):
                    modified_list.append(org_list[x])
            modified_list.append(org_list[1])
        else:
            if len(org_list) >= 2:
                for x in range(1,len(org_list),2):
                    modified_list.append(org_list[x])
    return

# Input 오류는 고려하지 않는다.
if __name__ == '__main__':
    solution(int(input()))
