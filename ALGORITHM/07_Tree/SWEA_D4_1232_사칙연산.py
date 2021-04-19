# 부모 노드가 있으면 계속 사칙연산
def four_rule_calculations(T):
    if len(T) <=2:
        return
    else:
        n2, v2, _, _ = T.pop()
        n1, v1, _, _ = T.pop()

        for k in range(1, len(T)):
            if n1 in T[k] and n2 in T[k]:
                if T[k][1] == '+':
                    T[k][1] = v1 + v2
                elif T[k][1] == '-':
                    T[k][1] = v1 - v2
                elif T[k][1] == '*':
                    T[k][1] = v1 * v2
                else:
                    T[k][1] = v1 / v2

        four_rule_calculations(T)



for tc in range(1):
    N = int(input())

    T = [[0,0,0,0] for _ in range(N+1)]
    for i in range(1,N+1):
        for j in input().split()[::-1]:
            try:
                T[i].insert(0, int(j))
                T[i].pop()
            except:
                T[i].insert(0,j)
                T[i].pop()

    four_rule_calculations(T)

    print(f'#{tc} {int(T[1][1])}')


############################################
# # input이 달라지면 시간이 줄어들까? --> 응 아냐~~ 오히려 더 길어짐
# for tc in range(1):
#     N = int(input())
#
#     T = [[] for _ in range(N+1)]
#     for i in range(1,N+1):
#         for j in input().split():
#             try:
#                 T[i].append(int(j))
#             except:
#                 T[i].append(j)
#         if len(T[i]) == 2:
#             T[i].extend([0,0])
#         elif len(T[i]) == 3:
#             T[i].append(0)
#
#     print(T)
#
#     four_rule_calculations(T)
#
#     print(f'#{tc} {int(T[1][1])}')
