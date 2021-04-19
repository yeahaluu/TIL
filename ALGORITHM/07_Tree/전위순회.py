def preorder_traverse(T):
    global v_list, visited
    if T:
        v, l, r = T.pop(0)
        visited.append(v)
        v_list[v] = [0, 0, 0]

        if l != 0:
            T.append(v_list[l])
            preorder_traverse(T)

        if r != 0:
            T.append(v_list[r])
            preorder_traverse(T)
    return



V = int(input())

arr = list(map(int, input().split()))

v_list = [[i, 0, 0] for i in range(V+1)]
for j in range(0, len(arr), 2):
    v_list[arr[j]].pop(1)
    v_list[arr[j]].append(arr[j+1])

# print(v_list)
visited = []

T = []
T.append(v_list[1])
preorder_traverse(T)

print(visited)
