# 16진수 -> 2진수
hex_list = {
    'A': 10,
    'B': 11,
    'C': 12,
    'D': 13,
    'E': 14,
    'F': 15,
}

b = []
arr = input()
for i in range(len(arr)):

    if arr[i].isalpha():
        hex = hex_list[arr[i]]
    else:
        hex = int(arr[i])

    for i in range(3, -1, -1):
        if hex & (1 << i):
            b.append(1)
        else:
            b.append(0)

# print(b)

# 2진수 -> 10진수

for i in range(0, len(b), 7):
    if i+7 > len(b):
        b2 = b[i::]
    else:
        b2 = b[i:i+7]

    result = 0
    n=1
    for j in range(len(b2)-1, -1, -1):
        if b2[j] & 1:
            result += b2[j]*n
        n *= 2


    if i < len(b)-7:
        print(result, end=', ')
    else:
        print(result)