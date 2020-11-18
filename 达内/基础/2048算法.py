def zero_to_end():
    # 数据排序，零往后
    for i in target_list:
        if i == 0:
            target_list.remove(i)
            target_list.append(0)


def merge():
    zero_to_end()
    for i in range(len(target_list) - 1):
        if target_list[i] == target_list[i + 1] and target_list[i] != 0:
            target_list[i] += target_list[i + 1]
            del target_list[i + 1]
            target_list.append(0)


def left_move():
    global target_list
    for line in map:
        target_list = line
        merge()


def right_move():
    global target_list
    for line in map:
        target_list = line[::-1]
        merge()
        line[::-1]=target_list

def square_matrix_transpose(sqr_matrix):
    for c in range(len(sqr_matrix) - 1):
        for r in range(c + 1, len(sqr_matrix)):
            sqr_matrix[r][c], sqr_matrix[c][r] = sqr_matrix[c][r], sqr_matrix[r][c]


def up_move():
    square_matrix_transpose(map)
    # 借助向左移动
    left_move()
    square_matrix_transpose(map)


def down_move():
    square_matrix_transpose(map)
    right_move()
    square_matrix_transpose(map)


target_list = [2, 0, 2, 0, 0, 8]
map = [[2, 0, 2, 0],
       [4, 4, 2, 0],
       [0, 4, 0, 4],
       [2, 2, 0, 4],
       ]
# __merge(list01)
# print(list01)
down_move()
print(map)
