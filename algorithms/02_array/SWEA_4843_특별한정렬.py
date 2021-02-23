import sys

sys.stdin = open('input_특별한정렬.txt', 'r')

for tc in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))

    for i in range(n):
        if i%2:
            min = i
            for j in range(i + 1, n):
                if arr[min] > arr[j]:
                    min = j
            arr[i], arr[min] = arr[min], arr[i]
        else:
            max_n = i
            for j in range(i + 1, n):
                if arr[max_n] < arr[j]:
                    max_n = j
            arr[i], arr[max_n] = arr[max_n], arr[i]
    print('#{}'.format(tc+1), end=' ')
    for i in arr[0:10]:
        print(i, end=' ')
    print()