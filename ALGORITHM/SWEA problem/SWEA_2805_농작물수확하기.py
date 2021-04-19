import sys

sys.stdin = open('input_농작물.txt', 'r')

for tc in range(1, int(input())+1):
    n = int(input())
    farm = [[int(i) for i in input()]for _ in range(n)]

    result = 0
    mid = n // 2

    for i in range(n//2+1):
        select = mid -i
        while select<=mid+i:
            result += farm[i][select]
            select +=1

    for j in range(n//2):
        select = mid - j
        while select <= mid + j:
            result += farm[n-1-j][select]
            select += 1

    print('#{} {}'.format(tc,result))
