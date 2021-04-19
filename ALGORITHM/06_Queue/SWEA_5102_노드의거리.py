# 거리 구하기
# BFS

for tc in range(1, int(input())+1):
    # V : 노드개수
    # E : 간선
    V, E = map(int,input().split())

    graph = [[]for _ in range(V+1)]

    for i in range(E):
        s, e = map(int,input().split())
        graph[s].append(e)
        graph[e].append(s)

    # S : 출발노드
    # G : 도착노드
    S, G = map(int,input().split())

    # 거리가 있는 방문록
    visited = [-1] * (V+1)

    Q = []
    dis = 0

    # 초기화설정
    Q.append(S)
    visited[S] = dis

    # Q가 없을때까지
    while Q:
        # 앞에서 하나 뽑아서 확인
        check = Q.pop(0)
        dis = visited[check] +1

        # check와 인접한거 전부 뽑아서
        for c in graph[check]:
            if visited[c] == -1:  # -1이면(방문하지 않았으면)
                Q.append(c)  # Q에 넣고
                visited[c] = dis  # 방문도장 쾅쾅

    # 가지 않은곳 -1로 해놨는데 연결 안되있으면 0 출력해야하니까...
    if visited[G] == -1:
        visited[G] = 0

    print('#{} {}'.format(tc,visited[G]))