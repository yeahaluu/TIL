# 힙삽입
def heap_insertion(T, v):
    n = len(T)  # 노드 번호
    T.append([n,v])
    change_mom_son(T, T[n][0], T[n][1])

# 삽입한 값을 자식 노드로 보고, 부모노드가 더 크다면 자리 바꾸기
def change_mom_son(T, son_n, son_v):
    mom_n = int((son_n)/2)
    if mom_n >= 1:
        mom_v = T[mom_n][1]
        if mom_v > son_v:
            T[mom_n][1], T[son_n][1] = son_v, mom_v
            change_mom_son(T, T[mom_n][0], T[mom_n][1])

# 부모노드들 다 더하기
def sum_mom_node(T, son_n):
    global mom_sum
    mom_n = int((son_n) / 2)
    if mom_n < 1:
        return
    else:
        mom_sum += T[mom_n][1]
        sum_mom_node(T, mom_n)


for tc in range(1, int(input()) + 1):
    N = int(input())
    # arr = list(map(int, input().split()))

    T = [[0,0]]  # 안 헷갈리게 0번 인덱스 만들어주기
    for v in input().split():
        heap_insertion(T, int(v))

    mom_sum = 0
    last_node = len(T)-1
    sum_mom_node(T, last_node)

    print(f'#{tc} {mom_sum}')




###########################################################
# 사실은 힙삽입 부분 없어도 되는데, 직관적이게 '힙'이라고 보고 싶어서 그냥 ...
#
# # 힙삽입
# # def heap_insertion(T, v):
# #     n = len(T)  # 노드 번호
# #     T.append([n,v])
# #     change_mom_son(T, T[n][0], T[n][1])
#
# # 삽입한 값을 자식 노드로 보고, 부모노드가 더 크다면 자리 바꾸기
# def change_mom_son(T, son_n, son_v):
#     mom_n = int((son_n)/2)
#     if mom_n >= 1:
#         mom_v = T[mom_n][1]
#         if mom_v > son_v:
#             T[mom_n][1], T[son_n][1] = son_v, mom_v
#             change_mom_son(T, T[mom_n][0], T[mom_n][1])
#
# # 부모노드들 다 더하기
# def sum_mom_node(T, son_n):
#     global mom_sum
#     mom_n = int((son_n) / 2)
#     if mom_n < 1:
#         return
#     else:
#         mom_sum += T[mom_n][1]
#         sum_mom_node(T, mom_n)
#
#
# for tc in range(1, int(input()) + 1):
#     N = int(input())
#     # arr = list(map(int, input().split()))
#
#     T = [[0,0]]  # 안 헷갈리게 0번 인덱스 만들어주기
#     for v in input().split():
#         # heap_insertion(T, int(v))
#         n = len(T)  # 노드 번호
#         T.append([n, int(v)])
#         change_mom_son(T, T[n][0], T[n][1])
#
#     mom_sum = 0
#     last_node = len(T)-1
#     sum_mom_node(T, last_node)
#
#     print(f'#{tc} {mom_sum}')



