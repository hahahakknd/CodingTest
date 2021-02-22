import sys

# Input 오류는 고려하지 않는다.
if __name__ == '__main__':
    loop_count: int = int(input())
    for num in range(0, loop_count):
        first_input: list = input().split(' ')
        second_input: list = input().split(' ')

        doc_count: int = int(first_input[0])
        doc_num_to_find: int = int(first_input[1])

        doc_lists: list = []
        for i in range(0, doc_count):
            doc_lists.append((int(second_input[i]), i))

        index: int = 0
        size: int = len(doc_lists)
        while index < size-1:
            if doc_lists[index][0] >= max(doc_lists[index+1:], key=lambda x:x[0])[0]:
                index += 1
                continue
            doc_lists.append(doc_lists.pop(index))

        print(list(map(lambda x:x[1], doc_lists)).index(doc_num_to_find)+1)
