import sys

sys.stdin = open('input_미로.txt', 'r')

dr = [0, 0, -1, 1]  # 상하좌우
dc = [-1, 1, 0, 0]

for tc in range(1, int(input()) + 1):
    N = int(input())
    maze = [[int(i) for i in input()] for i in range(N)]

    visited = [[] for i in range(N)]
    stack = []

    for row in range(N):
        for col in range(N):
            # 2 위치 찾기
            if maze[row][col] == 2:
                r_2 = row
                r_c = col
            # 3 위치 찾기
            elif maze[row][col] == 3:
                r_3 = row
                c_3 = col
            # 방문기록 만들기 1이면 T 아니면 F
            if maze[row][col] == 1:
                visited[row].append(True)
            else:
                visited[row].append(False)

    stack.append((r_2, r_c))

    while stack:
        now_r, now_c = stack.pop()
        # 4방탐색
        for i in range(4):
            fut_r = now_r + dr[i]
            fut_c = now_c + dc[i]
            if 0 <= fut_r <= N - 1 and 0 <= fut_c <= N - 1:
                if not visited[fut_r][fut_c]:
                    visited[fut_r][fut_c] = True
                    stack.append((fut_r, fut_c))

    if visited[r_3][c_3]:
        check = 1
    else:
        check = 0

    print('#{} {}'.format(tc,check))
