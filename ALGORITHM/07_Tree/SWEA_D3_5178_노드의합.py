# for tc in range(1, int(input()) + 1):
#     N, M, L = map(int, input().split())
#
#     # 각 노드의 번호(n)에 노드에 값(v)를 함께 적은 트리를 만든다
#     T = [[i, 0] for i in range(N + 1)]
#     for _ in range(M):
#         n, v = map(int, input().split())
#         T[n][1] = v
#
#     # 마지막 번호 노드부터 역순으로 자신의 부모 노드에 값을 더해준다
#     for i in range(N, 1, -1):
#         # if i * 2 + 1 > N:
#         #     T[i][1] = T[i * 2][1]
#         # else:
#         #     T[i][1] = T[i * 2][1] + T[i * 2 + 1][1]
#         T[i//2][1] += T[i][1]
#
#     print(f'#{tc} {T[L][1]}')


#############################################################
# 꼭 인덱스를 번호로 넣어줘야할까! 안하기 연습
# 안 나누고 역순으로 넣기
for tc in range(1, int(input()) + 1):
    N, M, L = map(int, input().split())

    # 각 노드의 번호를 인덱스로 해 노드에 값(v)를 함께 적은 트리를 만든다
    T = [0] *(N+1)
    for _ in range(M):
        n, v = map(int, input().split())
        T[n] = v

    # 마지막 번호 노드부터 역순으로 자신의 부모 노드에 값을 더해준다
    for i in range(N, 1, -1):
        T[i//2] += T[i]

    print(f'#{tc} {T[L]}')