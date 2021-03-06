# 아래 코드는 리커시브 에러 발생한 코드
# def makeSeq(sequence:list) -> list:
#     if len(sequence) <= 1:
#         return sequence

#     first_max_num_pos:int = 0
#     for index, value in enumerate(sequence):
#         if value > sequence[0]:
#             first_max_num_pos:int = index
#             break

#     root:list = [sequence[0]]
#     left:list = []
#     right:list = []

#     if first_max_num_pos == 0:  # 왼쪽노드만 있다.
#         left = makeSeq(sequence[1:])
#     elif first_max_num_pos == 1:  # 오른쪽노드만 있다.
#         right = makeSeq(sequence[1:])
#     else:
#         left = makeSeq(sequence[1:first_max_num_pos])
#         right = makeSeq(sequence[first_max_num_pos:])

#     return left + right + root

def makeSeq(sequence:list) -> list:
    answer:list = []
    sub_seq:list = sequence
    stack:list = []

    while len(answer) != len(sequence):
        if len(sub_seq) == 1:
            answer.append(sub_seq[0])
        elif len(sub_seq) > 1:
            first_max_num_pos:int = 0
            for index, value in enumerate(sub_seq):
                if value > sub_seq[0]:
                    first_max_num_pos:int = index
                    break

            stack.append([sub_seq[0]])
            if first_max_num_pos < 1:
                stack.append(sub_seq[1:])
            else:
                stack.append(sub_seq[first_max_num_pos:])
                stack.append(sub_seq[1:first_max_num_pos])

        if len(stack) == 0:
            break
        sub_seq = stack.pop()

    return answer

def solution(sequence: list) -> None:
    answer: list = makeSeq(sequence)
    for i in answer:
        print(i)
    return

# Input 오류는 고려하지 않는다.
if __name__ == '__main__':
    input_values: list = []
    while True:
        try:
            A: int = int(input())
            input_values.append(A)
        except EOFError:
            break
    solution(input_values)
