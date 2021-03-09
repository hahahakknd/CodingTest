def solution(chars) -> None:
    dials = [['A','B','C'],
             ['D','E','F'],
             ['G','H','I'],
             ['J','K','L'],
             ['M','N','O'],
             ['P','Q','R','S'],
             ['T','U','V'],
             ['W','X','Y','Z']]
    time = 0
    for c in chars:
        for i, dial in enumerate(dials):
            try:
                dial.index(c)
                time += (i+3)
                break
            except ValueError:
                pass
    print(time)
    return

# Input 오류는 고려하지 않는다.
if __name__ == '__main__':
    solution(input())
