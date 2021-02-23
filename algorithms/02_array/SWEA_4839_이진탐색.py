import sys

sys.stdin = open('input_이진탐색.txt', 'r')

for tc in range(int(input())):
    n, A, B = map(int, input().split())



    start = 1
    end = n
    countA = 0
    while start <= end:
        mid = (start + end) // 2
        if mid == A:
            break
        elif mid > A:
            end = mid
        else:
            start = mid
        countA += 1

    start = 1
    end = n
    countB = 0
    while start <= end:

        mid = (start + end) // 2
        if mid == B:
            break
        elif mid > B:
            end = mid
        else:
            start = mid
        countB += 1

    if countA > countB:
        print('#{} B'.format(tc + 1))
    elif countA < countB:
        print('#{} A'.format(tc + 1))
    else:
        print('#{} 0'.format(tc + 1))
