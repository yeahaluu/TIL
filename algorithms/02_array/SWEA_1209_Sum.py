import sys

sys.stdin = open('input_sum.txt', 'r')

for _ in range(10):
    tc = int(input())
    n = 100  # n * n 행렬
    arr = [[int(col) for col in input().split()] for row in range(n)]  # 5->100

    # 합들 저장할 리스트
    sum_lst = []

    # 가로 합 구하기
    for row in range(n):
        sum_num = 0
        for col in range(n):
            sum_num += arr[row][col]
        sum_lst.append(sum_num)

    # 세로 합 구하기
    for col in range(n):
        sum_num = 0
        for row in range(n):
            sum_num += arr[row][col]
        sum_lst.append(sum_num)

    # 대각선 합 구하기
    sum_num = 0
    for x in range(n):
        sum_num += arr[x][x]
    sum_lst.append(sum_num)

    # 역방향 대각선(?) 합
    sum_num = 0
    for y in range(n-1, -1, -1):
        sum_num += arr[y][y]
    sum_lst.append(sum_num)

    # 최대값 구하기
    max_num = sum_lst[0]
    for num in sum_lst:
        if max_num < num:
            max_num = num

    print('#{} {}'.format(tc, max_num))
