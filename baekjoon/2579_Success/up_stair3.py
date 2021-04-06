def solution() -> None:
    global stairs
    stairs_size = len(stairs)
    dp = []

    if stairs_size == 1:
        print(stairs[0])
        return
    if stairs_size == 2:
        print(max(stairs[0]+stairs[1], stairs[1]))
        return
    if stairs_size == 3:
        print(max(stairs[0]+stairs[2], stairs[1]+stairs[2]))
        return

    dp.append(stairs[0])
    dp.append(max(stairs[0]+stairs[1], stairs[1]))
    dp.append(max(stairs[0]+stairs[2], stairs[1]+stairs[2]))

    for i in range(3,stairs_size):
        dp.append(max(dp[i-2]+stairs[i], dp[i-3]+stairs[i-1]+stairs[i]))

    print(dp[stairs_size-1])
    return

# Input 오류는 고려하지 않는다.
if __name__ == '__main__':
    stairs = []
    loop_count = int(input())
    for _ in range(0, loop_count):
        stairs.append(int(input()))
    solution()
    # stairs = [10,20,15,25,10,20]
    # print(stairs)
    # solution()
