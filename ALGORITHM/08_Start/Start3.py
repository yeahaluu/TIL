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

#암호비트패턴
# 10진수 -> 2진수
n_list = [13, 19, 59, 49, 35, 55, 11, 61, 25, 47]

password_Bbit = []
for i in n_list:
    Bbit = []
    for j in range(5, -1, -1):
        if i & (1<<j):
            Bbit.append(1)
        else:
            Bbit.append(0)
    password_Bbit.append(Bbit)

# print(password_Bbit)

for i in range(len(b)):
    if b[i]:
        if b[i-2:i+4] in password_Bbit:
            b = b[i-2:]
        elif b[i-1:i+5] in password_Bbit:
            b = b[i-1:]
        elif b[i:i+6] in password_Bbit:
            b= b[i:]
        break

for i in range(0, len(b), 6):
    if i+6 > len(b):
        break
    else:
        b2 = b[i:i+6]
        result = 0
        n=1
        for j in range(len(b2)-1, -1, -1):
            if b2[j] & 1:
                result += b2[j]*n
            n *= 2

    for k in range(len(n_list)):
        if result == n_list[k]:
            if i < len(b) - 11:
                print(k, end=', ')
            else:
                print(k)
