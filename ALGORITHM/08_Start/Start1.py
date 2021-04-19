# 2진수 -> 10진수 (7비트씩 끊어서)

data = list(map(int, input()))

for i in range(0, len(data), 7):
    data2 = data[i:i+7]
    result = 0
    n=1
    for j in range(6, -1, -1):
        if data2[j] & 1:
            result += data2[j]*n
        n *= 2

    if i < len(data)-7:
        print(result, end=', ')
    else:
        print(result)
