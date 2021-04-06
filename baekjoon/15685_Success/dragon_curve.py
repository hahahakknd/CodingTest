# 좌료는 (0,0) 을 기준으로 계산된다.
#
# 반시계방향 변환함수
# |x| = |cos90 -sin90||x`|
# |y|   |sin90  cos90||y`|
#
# 반시계방향
# |x| = |0 -1||x`|
# |y|   |1  0||y`|
#
# 시계방향
# |x| = |0  1||x`|
# |y|   |-1 0||y`|
#
# dragon_curve_point = (1*y`, -1*x`)

def dragon_curve(starting_point:list, direction:int, gen_count:int) -> list:
    points = [starting_point]
    if direction == 0:    # 오른쪽
        points.append([starting_point[0]+1, starting_point[1]])
    elif direction == 1:  # 위쪽
        points.append([starting_point[0], starting_point[1]+1])
    elif direction == 2:  # 왼쪽
        points.append([starting_point[0]-1, starting_point[1]])
    elif direction == 3:  # 아래쪽
        points.append([starting_point[0], starting_point[1]-1])
    else:
        raise RuntimeError()

    curve_points = []
    for _ in range(gen_count):
        last_postion = len(points)-1
        differ_point = [-x for x in points[last_postion]]
        curve_points.clear()
        for pos in range(last_postion-1,-1,-1):
            curve_points.append([points[pos][1]+differ_point[1]-differ_point[0], -(points[pos][0]+differ_point[0])-differ_point[1]])
        points.extend(curve_points)
    return points

def merge_dragon_curves(dragon_curves:list) -> list:
    merged_dragon_curve = []
    for dragon_curve in dragon_curves:
        for point in dragon_curve:
            try:
                merged_dragon_curve.index(point)
            except ValueError:
                merged_dragon_curve.append(point)
    return merged_dragon_curve

def find_square(merged_dragon_curve:list) -> int:
    square_count = 0
    for point in merged_dragon_curve:
        try:
            merged_dragon_curve.index([point[0]+1,point[1]])
            merged_dragon_curve.index([point[0],point[1]-1])
            merged_dragon_curve.index([point[0]+1,point[1]-1])
            square_count += 1
        except ValueError:
            pass
    return square_count

def solution(inputs: list) -> None:
    dragon_curves = []
    for input in inputs:
        dragon_curves.append(dragon_curve([input[0],-input[1]], input[2], input[3]))
    print(find_square(merge_dragon_curves(dragon_curves)))
    return

# Input 오류는 고려하지 않는다.
if __name__ == '__main__':
    input_list: list = []
    loop_count: int = int(input())
    for _ in range(0, loop_count):
        input_list.append([int(x) for x in input().split(' ')])
    solution(input_list)
    # solution([[3,3,0,1],[4,2,1,3],[4,2,2,1]])
    # solution([[3,3,0,1],[4,2,1,3],[4,2,2,1],[2,7,3,4]])
    # solution([[5,5,0,0],[5,6,0,0],[5,7,0,0],[5,8,0,0],[5,9,0,0],[6,5,0,0],[6,6,0,0],[6,7,0,0],[6,8,0,0],[6,9,0,0]])
    # solution([[50,50,0,10],[50,50,1,10],[50,50,2,10],[50,50,3,10]])
