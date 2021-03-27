import sys
sys.stdin = open('input_파리퇴치.txt', 'r')

for tc in range(int(input())):
    N, M = map(int, input().split())
    arr = [[int(i) for i in input().split()] for _ in range(N)]

    col = 0
    row = 0

    sum_lst = []
    max_n = -1 << 40
    for b_row in range(N - M + 1):
        for b_col in range(N - M + 1):
            sum_n = 0
            for s_row in range(b_row, M + b_row):
                for s_col in range(b_col, M + b_col):
                    sum_n += arr[s_row][s_col]
            if sum_n > max_n:
                max_n = sum_n

    print('#{} {}'.format(tc + 1, max_n))
