# 중위순회(but 순서x, i 하나씩 증가해서 node의 값으로 넣는다)
def inorder_transform(root, N):
    global i
    if root <= N:
        inorder_transform(root * 2, N)
        i += 1
        node_value[root].append(i)
        inorder_transform(root * 2 + 1, N)


for tc in range(1, int(input()) + 1):
    N = int(input())

    # node_value에 노드 번호를 넣는다.
    node_value = [[i] for i in range(N + 1)]

    i = 0
    inorder_transform(1, N)

    print(f'#{tc} {node_value[1][1]} {node_value[int(N/2)][1]}')


