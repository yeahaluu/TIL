import sys
sys.stdin = open('input_삼성시버스노선.txt', 'r')

for tc in range(int(input())):
    n = int(input())
    a = []
    b = []
    for i in range(n):
        ai, bi = map(int,input().split())
        a += [ai]
        b += [bi]
    p_n = int(input())
    p = [0] * p_n
    for i in range(p_n):
        p[i] += int(input())

    count_p = [0] * p_n
    for i in range(n):
        for j in range(p_n):
            if a[i]<= p[j] <= b[i]:
                count_p[j] += 1


    print('#{}'.format(tc+1), end=' ')
    for i in range(p_n-1):
        print(count_p[i],end=' ')
    print(count_p[p_n-1])


