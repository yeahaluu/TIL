# 나이트가 이동할 수 있는 위치
dr = [-2, -2, -1, 1, 2, 2, 1, -1]
dc = [-1, 1, 2, 2, 1, -1, -2, -2]


for tc in range(1, int(input())+1):
    I = int(input())
    s_r, s_c = map(int,input().split()) # 시작점
    g_r, g_c = map(int, input().split()) # 도착점

    # 방문록 (거리 입력)
    visited = [[-1 for _ in range(I)] for _ in range(I)]
    Q = []

    dis = 0 # 거리
    visited[s_r][s_c] = dis

    Q.append((s_r, s_c, dis))

    # 같은 자리일 때!
    if s_r == g_r and s_c== g_c:
        dis = 0
        Q = 0

    while Q:
        n_r, n_c, dis = Q.pop(0)
        dis += 1

        # 8방탐색
        for k in range(8):
            fut_r = n_r +dr[k]
            fut_c = n_c +dc[k]

            # 탐색한 위치에 방문도장이 안 찍혀 있으면?
            if 0<= fut_r < I and 0<= fut_c < I:

                if fut_r == g_r and fut_c == g_c:
                    Q = []
                    break
                elif visited[fut_r][fut_c] == -1:
                    visited[fut_r][fut_c] = dis # 방문도장 찍어주기
                    Q.append((fut_r, fut_c, dis))  # Q에 위치 넣기

    print(dis)
