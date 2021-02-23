import sys
sys.stdin = open('input_어디에단어.txt', 'r')

for tc in range(int(input())):
    N, K = map(int, input().split())
    arr = [[int(i) for i in input().split()] for _ in range(N)]

    w_count = 0
    for i in range(N):
        k_count = 1
        for j in range(N-1):
            if arr[i][j] == 1 and arr[i][j+1] == 1:
                k_count += 1
            else:
                if k_count == K:
                    w_count += 1
                k_count = 1
        if k_count == K:
            w_count += 1

    for i in range(N):
        k_count = 1
        for j in range(N - 1):
            if arr[j][i] == 1 and arr[j+1][i] == 1:
                k_count += 1
            else:
                if k_count == K:
                    w_count += 1
                k_count = 1
        if k_count == K:
            w_count += 1
    print('#{} {}'.format(tc+1, w_count))


