
# 중위순회
def inorder_traverse(v):
    if v:
        inorder_traverse(arr[v][2])
        result.append(arr[v][1])
        inorder_traverse(arr[v][3])



for tc in range(1):
    N = int(input())

    # int, string 구분해서 넣기 & 각 리스트가 4개의 원소를 가지고 원소가 없으면 0추가
    arr = [[0, 0, 0, 0] for _ in range(N+1)]
    for i in range(1, N+1):
        for j in input().split()[::-1]:
            try:
                arr[i].insert(0, int(j))
                arr[i].pop()
            except:
                arr[i].insert(0,j)
                arr[i].pop()


    result = [] # 순서 출력
    inorder_traverse(1)


    print('#{}'.format(tc), end=' ')
    for s in result:
        print(s, end='')
    print()