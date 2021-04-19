# BFS
dr = [0, 0, -1, 1]  # 상하좌우
dc = [-1, 1, 0, 0]

for tc in range(1, int(input()) + 1):
    N = int(input())
    maze = [[int(i) for i in input()] for _ in range(N)]

    visited = [[] for _ in range(N)]
    Q = []

    for row in range(N):
        for col in range(N):
            # 시작점 찾기
            if maze[row][col] == 2:
                r_2 = row
                c_2 = col
            # 도착점 찾기
            elif maze[row][col] == 3:
                r_3 = row
                c_3 = col
            # visited 만들기
            if maze[row][col] == 1:
                visited[row].append(-2)  # 벽
            else:
                visited[row].append(-1)  # 안 갔다

    dis = 0  # 거리
    visited[r_2][c_2] = dis

    # 시작점 입력
    Q.append((r_2, c_2, dis))

    while Q:
        now_r, now_c, dis = Q.pop(0)

        # 4방탐색
        for k in range(4):
            fut_r = now_r + dr[k]
            fut_c = now_c + dc[k]

            # 탐색한 위치가 방문도장이 안 찍혀 있으면
            if 0 <= fut_r <= N - 1 and 0 <= fut_c <= N - 1:
                if visited[fut_r][fut_c] == -1:
                    Q.append((fut_r, fut_c, dis+1))  # Q에 위치를 넣고
                    visited[fut_r][fut_c] = dis + 1  # 방문도장을 거리로 찍어준다

    # print(maze)
    # print(visited)
    if visited[r_3][c_3]==-1:
        print('#{} 0'.format(tc))
    else:
        print('#{} {}'.format(tc, visited[r_3][c_3]-1))  # 가는데 있는 0의 수니까 -1 해준다


