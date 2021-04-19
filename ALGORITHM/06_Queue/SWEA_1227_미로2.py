import sys
sys.stdin = open('input_미로2.txt','r')

dr = [0, 0, -1, 1]  # 상하좌우
dc = [-1, 1, 0, 0]

for _ in range(1, 11):
    tc = int(input())
    maze = [[int(i) for i in input()] for _ in range(100)]

    visited = maze

    for row in range(100):
        for col in range(100):
            if maze[row][col] == 2:
                r_2 = row
                c_2 = col
            elif maze[row][col] == 3:
                r_3 = row
                c_3 = col

    Q = []

    # 초기화 설정
    Q.append((r_2,c_2))
    visited[r_2][c_2] = 1

    while Q:
        now_r, now_c = Q.pop(0)

        # 4방탐색
        for k in range(4):
            fut_r = now_r + dr[k]
            fut_c = now_c + dc[k]

            # 탐색한 위치가 방문도장이 안 찍혀 있으면
            if 0 <= fut_r <= 99 and 0 <= fut_c <= 99:
                if not visited[fut_r][fut_c] == 1:
                    Q.append((fut_r, fut_c))  # Q에 위치를 넣고
                    visited[fut_r][fut_c] = 1  # 방문도장을 거리로 찍어준다
    if visited[r_3][c_3] == 1:
        check= 1
    else:
        check = 0

    print('#{} {}'.format(tc, check))