import sys

sys.stdin = open('input_숫자를정렬.txt', 'r')

for tc in range(int(input())):
    N = int(input())
    arr = list(map(int, input().split()))

    for i in range(N-1):
        min_idx = i
        for j in range(i+1, N):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[min_idx], arr[i] = arr[i], arr[min_idx]

    print('#{}'.format(tc+1), end = ' ')
    print(*arr)