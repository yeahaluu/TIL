# 1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7

# BFS 경로 출력
def my_BFS(graph, v):  # 그래프랑 시작점 v

    # 방문록 생성
    visited = [False] * len(graph)

    # 큐 생성
    queue = []
    # 경로 저장할 route 생성
    route = []

    # 큐에 시작점 새기기 (위의 작업과 함께 해도 됨)
    queue.append(v)
    # 경로에 경로 적기
    route.append(v)
    # 이와 함께 방문도장도 쾅쾅!
    visited[v] = True

    # 큐에 아무것도 없을때 까지 반복
    while queue:
        # 큐에서 front를 가져와!
        tmp = queue.pop(0)

        # tmp와 붙어 있는 것들 전부 넣자!
        for t in graph[tmp]:
            if visited[t] == False:
                queue.append(t)
                route.append(t)
            visited[t] = True

    return route

ip = list(map(int,input().split()))
graph = [[]for _ in range(max(ip)+1)]


for i in range(0,len(ip),2):
    x = ip[i]
    graph[x].append(ip[i+1])


print(*my_BFS(graph,1))



