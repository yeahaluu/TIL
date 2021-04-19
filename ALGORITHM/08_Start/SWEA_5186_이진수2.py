# 소수점: 10진수 -> 2진수
for tc in range(1, int(input())+1):
    decimal = float(input())
    binary = []

    for i in range(1, 13):
        if decimal >= 2 ** -i:
            decimal -= 2 ** -i
            binary.append(1)
        else:
            binary.append(0)
        if decimal == 0:
            break

    if decimal:
        print(f'#{tc} overflow')
    else:
        print(f'#{tc}', end=' ')
        for i in binary:
            print(i, end='')
        print()