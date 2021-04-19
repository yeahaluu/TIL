import sys

sys.stdin = open('input_오셀로.txt', 'r')

for tc in range(1, int(input()) + 1):

    n, m = map(int, input().split())

    game_board = [[0] * n for _ in range(n)]
    game_board[n // 2][n // 2] = 2
    game_board[n // 2 - 1][n // 2 - 1] = 2
    game_board[n // 2 - 1][n // 2] = 1
    game_board[n // 2][n // 2 - 1] = 1

    dr = [-1, -1, -1, 0, 1, 1, 1, 0]  # 북서/북/북동/동/남동/남/남서/서
    dc = [-1, 0, 1, 1, 1, 0, -1, -1]


    for i in range(m):
        col, row, color = map(int, input().split())
        game_board[row - 1][col - 1] = color

        # 8방향 탐색!!
        for k in range(len(dr)):
            x = dr[k]
            y = dc[k]

            # 탐색한 값은 게임보드 안에 존재해야한다.
            if 0 <= row - 1 + x <= n - 1 and 0 <= col - 1 + y <= n - 1:

                # 내 돌이 흑들, 바로 옆의 돌이 백돌일 때
                if game_board[row - 1][col - 1] == 1 and game_board[row - 1 + x][col - 1 + y] == 2:
                    # n-1만큼 그 방향으로 한칸씩 가보자.
                    for j in range(1,n):

                        # 그 방향으로 j만큼 움직인 값은 게임보드 내에 있어야한다.
                        if 0 <= row - 1 + x * j <= n - 1 and 0 <= col - 1 + y * j <= n - 1:

                            # j만큼 움직인 값이 흑돌이면!!!!!
                            if game_board[row - 1 + x *j][col-1+y*j]==1:
                                l = 1
                                # j 만큼 가면서 가면서 백돌인 값 흑돌로 바꾸기
                                while game_board[row-1+x*l][col-1+y*l] == 2 and l<j:
                                    game_board[row-1+x*l][col-1+y*l] = 1
                                    l +=1
                            elif game_board[row - 1 + x *j][col-1+y*j]==0:
                                break

                # 내돌이 백돌, 바로 옆의 돌이 흑돌일때,
                elif game_board[row - 1][col - 1] == 2 and game_board[row - 1 + x][col - 1 + y] == 1:
                    # n-1만큼 그 방향으로 한칸씩 가보자
                    for j in range(1, n):

                        # 그 방향만큼 j만큼 움직인 값은 게임보드 내에 있어야 한다.
                        if 0 <= row - 1 + x * j <= n - 1 and 0 <= col - 1 + y * j <= n - 1:
                            # j만큼 움직인 값이 백돌이면!!!
                            if game_board[row - 1 + x *j][col-1+y*j]==2:
                                l = 1
                                # j 만큼 가면서 (
                                while game_board[row-1+x*l][col-1+y*l] == 1 and l<j:
                                    game_board[row-1+x*l][col-1+y*l] = 2
                                    l+=1
                            elif game_board[row - 1 + x *j][col-1+y*j]==0:
                                break

        # print(col, row, color, game_board)
    black = 0
    white = 0
    for i in range(n):
        for j in range(n):
            if game_board[i][j] ==1:
                    black +=1
            elif game_board[i][j] ==2:
                    white +=1

    print('#{} {} {}'.format(tc,black,white))
