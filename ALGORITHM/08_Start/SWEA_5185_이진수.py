# 16진수 -> 2진수
hex_list = '0123456789ABCDEF'

for tc in range(1, int(input())+1):
    b = []
    N, arr = input().split()

    for s in arr:
        decimal = hex_list.index(s)
        for i in range(3, -1, -1):
            if decimal & (1 << i):
                b.append(1)
            else:
                b.append(0)

    print(f'#{tc}', end=' ')
    for i in b:
        print(i, end='')
    print()