import sys

class LinkedList:
    def __init__(self, value):
        self.value = value
        self.front = None
        self.rear = None

def solution(input):
    global CURSOR
    if input[0] == 'L':
        if CURSOR.front != None:
            CURSOR = CURSOR.front
    elif input[0] == 'D':
        if CURSOR.rear != None:
            CURSOR = CURSOR.rear
    elif input[0] == 'B':
        if CURSOR.front != None:
            front_cursor = CURSOR.front
            rear_cursor = CURSOR.rear
            front_cursor.rear = rear_cursor
            if rear_cursor != None:
                rear_cursor.front = front_cursor
            CURSOR = front_cursor
    elif input[0] == 'P':
        front_cursor = CURSOR
        center_cursor = LinkedList(input[1])
        rear_cursor = CURSOR.rear
        front_cursor.rear = center_cursor
        center_cursor.front = front_cursor
        center_cursor.rear = rear_cursor
        if rear_cursor != None:
            rear_cursor.front = center_cursor
        CURSOR = center_cursor
    return

# Input 오류는 고려하지 않는다.
if __name__ == '__main__':
    global CURSOR
    CURSOR = LinkedList(None)
    FIRST_CURSOR = CURSOR
    for i in sys.stdin.readline().rstrip():
        front_cursor = CURSOR
        CURSOR.rear = LinkedList(i)
        CURSOR = CURSOR.rear
        CURSOR.front = front_cursor
    loop_count = int(sys.stdin.readline().rstrip())
    for _ in range(loop_count):
        solution(sys.stdin.readline().rstrip().split(' '))
    CURSOR = FIRST_CURSOR.rear
    print_str = ''
    while CURSOR != None:
        print_str += CURSOR.value
        CURSOR = CURSOR.rear
    print(print_str)
    # CURSOR = LinkedList(None)
    # FIRST_CURSOR = CURSOR
    # for i in 'abcd':
    #     front_cursor = CURSOR
    #     CURSOR.rear = LinkedList(i)
    #     CURSOR = CURSOR.rear
    #     CURSOR.front = front_cursor
    # solution(['P','x'])
    # solution(['L'])
    # solution(['P','y'])
    # CURSOR = FIRST_CURSOR.rear
    # print_str = ''
    # while CURSOR != None:
    #     print_str += CURSOR.value
    #     CURSOR = CURSOR.rear
    # print(print_str)
    # CURSOR = LinkedList(None)
    # FIRST_CURSOR = CURSOR
    # for i in 'abc':
    #     front_cursor = CURSOR
    #     CURSOR.rear = LinkedList(i)
    #     CURSOR = CURSOR.rear
    #     CURSOR.front = front_cursor
    # solution(['L'])
    # solution(['L'])
    # solution(['L'])
    # solution(['L'])
    # solution(['L'])
    # solution(['P','x'])
    # solution(['L'])
    # solution(['B'])
    # solution(['P','y'])
    # CURSOR = FIRST_CURSOR.rear
    # print_str = ''
    # while CURSOR != None:
    #     print_str += CURSOR.value
    #     CURSOR = CURSOR.rear
    # print(print_str)
    # CURSOR = LinkedList(None)
    # FIRST_CURSOR = CURSOR
    # for i in 'dmih':
    #     front_cursor = CURSOR
    #     CURSOR.rear = LinkedList(i)
    #     CURSOR = CURSOR.rear
    #     CURSOR.front = front_cursor
    # solution(['B'])
    # solution(['B'])
    # solution(['P','x'])
    # solution(['L'])
    # solution(['B'])
    # solution(['B'])
    # solution(['B'])
    # solution(['P','y'])
    # solution(['D'])
    # solution(['D'])
    # solution(['P','z'])
    # CURSOR = FIRST_CURSOR.rear
    # print_str = ''
    # while CURSOR != None:
    #     print_str += CURSOR.value
    #     CURSOR = CURSOR.rear
    # print(print_str)
    # CURSOR = LinkedList(None)
    # FIRST_CURSOR = CURSOR
    # for i in 'abcd':
    #     front_cursor = CURSOR
    #     CURSOR.rear = LinkedList(i)
    #     CURSOR = CURSOR.rear
    #     CURSOR.front = front_cursor
    # solution(['B'])
    # solution(['B'])
    # solution(['B'])
    # solution(['B'])
    # solution(['B'])
    # CURSOR = FIRST_CURSOR.rear
    # print_str = ''
    # while CURSOR != None:
    #     print_str += CURSOR.value
    #     CURSOR = CURSOR.rear
    # print(print_str)
