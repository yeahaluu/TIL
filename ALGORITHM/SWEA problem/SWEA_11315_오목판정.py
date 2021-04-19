import sys

sys.stdin = open('input_오목.txt', 'r')

for tc in range(1, int(input()) + 1):
    n = int(input())
    arr = [[i for i in input()] for _ in range(n)]

    for i in range(n):
        arr[i] = [0] + arr[i] + [0]
    arr = [[0] * (n + 2)] + arr + [[0] * (n + 2)]

    dr = [1, 1, 1, 0]  # 남동/남/남서/서 : 절반만 봐도 된다.
    dc = [-1, 0, 1, 1]

    result = 'NO'
    # 완전 탐색
    for row in range(1, n + 1):
        for col in range(1, n + 1):

            # 만약 그 중 o인게 나오면
            if arr[row][col] == 'o':
                current = arr[row][col]
                count =1
                # 상하좌우 대각선 방향에 o가 또 있는지 확인해보자
                for i in range(4):
                    x = dr[i]
                    y = dc[i]

                    # 움직인 값은 범위를 벗어나면 안돼!
                    if 1 <= row + x <= n and 1 <= col + y <= n:
                        # count 위치
                        count = 1
                        # o가 있으면! 같은 방향으로 o가 계속 있는지 확인
                        if arr[row + x][col + y] == 'o':
                            count += 1
                            current_row = row + x
                            current_col = col + y

                            while arr[current_row + x][current_col + y] == 'o':
                                count += 1
                                current_row += x
                                current_col += y
                    # if 위치
                    if count >= 5:
                        result = 'YES'
                        break
    print('#{} {}'.format(tc,result))