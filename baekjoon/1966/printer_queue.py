import sys

def find_order(sorted_doc_lists: list, doc_num: int) -> int:
    for j in range(0, len(sorted_doc_lists)):
        print(str(sorted_doc_lists[j][0]) + ', ' + str(sorted_doc_lists[j][1]))

    start: int = 0
    end: int = len(sorted_doc_lists) - 1
    index: int = len(sorted_doc_lists) // 2
    while True:
        found_num: int = sorted_doc_lists[index][0]
        if found_num < doc_num:
            start = index + 1
            index =




    for j in range(0, len(sorted_doc_lists)):
        print(str(sorted_doc_lists[j][0]) + ', ' + str(sorted_doc_lists[j][1]))
    return sorted_doc_lists.index(lambda doc_num: doc_num[0])

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
            doc_lists.append((i, int(second_input[i])))

        print(find_order(sorted(doc_lists, key=lambda doc: doc[1]), doc_num_to_find))
