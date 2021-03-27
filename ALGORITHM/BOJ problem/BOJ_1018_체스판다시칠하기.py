N, M = map(int, input().split())

board = [[s for s in input()] for _ in range(N)]

dif_sum_lst = []



for row in range(N - 8 + 1):
    for col in range(M - 8 + 1):

        dif_sum = 0

        for in_row in range(row, row + 8):
            for in_col in range(col, col + 8):
                # 왼쪽위 행을 %2한 값이 내부 행의 %2한 값과 같고
                if row % 2 == in_row % 2:
                    # 왼쪽위 열을 %2한 값이 내부 열의 %2한 값과 같으면 같은 색이여야한다.
                    if col % 2 == in_col % 2:
                        # 다른 색이면 +1
                        if board[row][col] != board[in_row][in_col]:
                            dif_sum += 1
                    else:
                        if board[row][col] == board[in_row][in_col]:
                            dif_sum += 1
                # 왼쪽위 행을 %2한 값이 내부 행의 %2한 값과 다르고
                else:
                    # 왼쪽위 열을 %2한 값이 내부 열의 %2한 값과 다르면 같은 색이다.
                    if col % 2 != in_col % 2:
                        # 두 색이 다르면 +1
                        if board[row][col] != board[in_row][in_col]:
                            dif_sum += 1
                    else:
                        if board[row][col] == board[in_row][in_col]:
                            dif_sum += 1
        #####
        dif_sum_reserve = 64-dif_sum
        dif_sum_lst.append(dif_sum)
        dif_sum_lst.append(dif_sum_reserve)

print(min(dif_sum_lst))


