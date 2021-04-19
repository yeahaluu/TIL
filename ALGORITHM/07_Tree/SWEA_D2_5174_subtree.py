# 오른쪽이나 왼쪽에 자식노드가 있으면 count
def subtree_count(N):
    global cnt
    cnt +=1
    if T[N][0]:
        subtree_count(T[N][0])
    if T[N][1]:
        subtree_count(T[N][1])

for tc in range(1, int(input())+1):
    E, N = map(int,input().split())
    arr = list(map(int, input().split()))

    # 각 인덱스에 왼쪽, 오른쪽 자식 노드 값을 입력(없으면 0)
    T = [[0, 0] for _ in range(E+2)]
    for i in range(0, E*2, 2):
        T[arr[i]].insert(0, arr[i+1])
        T[arr[i]].pop()

    cnt = 0
    subtree_count(N)

    print(f'#{tc} {cnt}')


###########################################################
# global없이 해보기

# def subtree_count(N, cnt):
#     cnt +=1
#     if T[N][0]:
#         l, T[N][0] = T[N][0], 0
#         cnt = subtree_count(l, cnt)
#     if T[N][1]:
#         r, T[N][1] = T[N][1], 0
#         cnt = subtree_count(r, cnt)
#     return cnt
#
# for tc in range(1, int(input())+1):
#     E, N = map(int,input().split())
#     arr = list(map(int, input().split()))
#
#     # 각 인덱스에 왼쪽, 오른쪽 자식 노드 값을 입력(없으면 0)
#     T = [[0, 0] for _ in range(E+2)]
#     for i in range(0, E*2, 2):
#         T[arr[i]].insert(0, arr[i+1])
#         T[arr[i]].pop()
#
#     cnt = 0
#     cnt = subtree_count(N, cnt)
#
#     print(f'#{tc} {cnt}')


