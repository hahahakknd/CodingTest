import sys

def whereIsCheckinRoom(height: int, customer_number: int) -> int:
    quotient: int = customer_number//height
    remainder: int = customer_number%height

    # 나누어 떨어지는 케이스
    if remainder == 0:
        room_number: int = quotient
        floor_number: int = height
    else: # 나누어 떨어지지 않는 케이스
        room_number: int = quotient + 1
        floor_number: int = remainder

    return (floor_number*100) + (room_number)

if __name__ == '__main__':
    loop_count: int = int(input())
    for num in range(0, loop_count):
        checkin_info: list = input().split(' ')
        print(whereIsCheckinRoom(int(checkin_info[0]), int(checkin_info[2])))
