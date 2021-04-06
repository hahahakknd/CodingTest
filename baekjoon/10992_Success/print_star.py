import sys

class LineMaker:
    def __init__(self, max_line_number: int):
        super().__init__()

        if max_line_number < 1:
            raise Exception(f'The max line number({max_line_number}) is less than 1.')

        self._max_line_number: int = max_line_number
        self._max_star_count: int = (2 * max_line_number) - 1
        self._first_line_star_postion: int = (self._max_star_count // 2) + 1

    def make_line(self, line_number: int) -> str:
        if line_number > self._max_line_number:
            raise Exception(f'The line number({line_number}) \
                              is over the max line number({self._max_line_number}).')

        line_str: str = ''

        # 삼각형의 마지막 줄이면 전부 별을 찍는다.
        if line_number == self._max_line_number:
            for postion in range(1, self._max_star_count+1):
                line_str += '*'
            return line_str

        # 별이 찍히는 위치를 계산한다.
        if line_number == 1:
            first_star_postion: int = self._first_line_star_postion
            second_star_postion: int = self._first_line_star_postion
        else:
            first_star_postion: int = self._first_line_star_postion - (line_number - 1)
            second_star_postion: int = self._first_line_star_postion + (line_number - 1)

        for postion in range(1, second_star_postion+1):
            if postion in (first_star_postion, second_star_postion):
                line_str += '*'
            else:
                line_str += ' '

        return line_str

if __name__ == '__main__':
    input_number: int = int(input())
    line_maker: LineMaker = LineMaker(input_number)

    for i in range(1, input_number+1):
        print(line_maker.make_line(i))
