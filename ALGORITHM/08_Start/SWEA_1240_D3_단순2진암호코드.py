#암호비트패턴
# 10진수 -> 2진수
n_list = [13, 25, 19, 61, 35, 49, 47, 59, 55, 11]

password_Bbit = []
for i in n_list:
    Bbit = []
    for j in range(6, -1, -1):
        if i & (1<<j):
            Bbit.append(1)
        else:
            Bbit.append(0)
    password_Bbit.append(Bbit)


for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    zero = [0 for _ in range(M)]
    for _ in range(N):
        lst = list(map(int, input()))
        if lst != zero:
            for i in range(M-1, -1, -1):
                if lst[i] == 1 and lst[i-6:i+1] in password_Bbit:
                    b = lst[i-55:i+1]
                    result = []
                    for i in range(0, len(b), 7):

                        b2 = b[i:i + 7]
                        result_num = 0
                        n = 1
                        for j in range(len(b2) - 1, -1, -1):
                            if b2[j] & 1:
                                result_num += b2[j] * n
                            n *= 2
                        for k in range(len(n_list)):
                            if result_num == n_list[k]:
                                result.append(k)
                    n1, n2, real_result = 0, 0, 0
                    for k in range(7):
                        if k%2:
                            n2 += result[k]
                        else:
                            n1 += result[k]
                        real_result += result[k]
                    n = n1*3 + n2 + result[7]
                    if n%10==0:
                        real_result += result[7]
                    else:
                        real_result = 0

                    break
            # break
    print(f'#{tc} {real_result}')