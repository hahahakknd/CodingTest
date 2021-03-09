def solution() -> None:
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
    solution()
