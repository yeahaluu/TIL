# 기지국이 커버칠 수 없는 집 찾기
import sys

sys.stdin = open('input_기지국.txt', 'r')

for tc in range(1, int(input())+1):
    n = int(input())

    # n*n 마을
    # H : 집
    # A : 기지국
    town = [[s for s in input()] for _ in range(n)]

    # print(town)

    dr = [-1,1,0,0]#상하좌우
    dc = [0,0,-1,1]
    # 기지국의 열과 행 뽑아내!
    A_rows = []
    A_cols = []

    for row in range(n):
        for col in range(n):
            if town[row][col]== 'A':
                for k in range(4):
                    if 0 <= row + dr[k] <= n - 1 and 0 <= col + dc[k] <= n - 1:
                        town[row+dr[k]][col+dc[k]] = 'X'
            if town[row][col]== 'B':
                for k in range(4):
                    for i in range(1,3):
                        if 0 <= row + dr[k] * i <= n - 1 and 0 <= col + dc[k] * i <= n - 1:
                            town[row+dr[k]*i][col+dc[k]*i] = 'X'
            if town[row][col]== 'C':
                for k in range(4):
                    for i in range(1,4):
                        if 0<=row+dr[k]*i<=n-1 and 0<=col+dc[k]*i<=n-1:
                            town[row+dr[k]*i][col+dc[k]*i] = 'X'
    count = 0
    for row in range(n):
        for col in range(n):
            if town[row][col] == 'H':
                count +=1

    print('#{} {}'.format(tc,count))



