dr = [-1, 1, 0, 0]  # 상하좌우
dc = [0, 0, -1, 1]


N = int(input())
villages = [[int(i) for i in input().split()] for _ in range(N)]


village_list = []
# villages 높이의 최소, 최대값 구하기
for row in range(0, N):
    for col in range(0, N):
        village_list.append(villages[row][col])
village_list = sorted(list(set(village_list)))
village_list = [0] + village_list[0:-1]


cnt_list = []
# 그 높이를 다 돌아가면서 각각의 안전영역 구하기
for j in village_list:  # j: 물의 높이

    # 물이 잠기는 곳 0으로 만들기
    copy_villages = [[] for _ in range(N)]
    cnt = 0
    for row in range(0, N):
        for col in range(0, N):
            if villages[row][col] <= j:
                copy_villages[row].append(0)
            else:
                copy_villages[row].append(villages[row][col])

    for row in range(0, N):
        for col in range(0, N):
            # 0이 아닌 곳이 나오면 stack에 저장
            stack = []
            if copy_villages[row][col] != 0:
                cnt +=1
                stack.append((row, col))
                copy_villages[row][col] = 0  # 방문도장

                # stack에 무언가 없어질 때 까지!
                while stack:
                    select_row, select_col = stack.pop()

                    # 4방 탐색
                    for k in range(4):
                        new_row = select_row + dr[k]
                        new_col = select_col + dc[k]
                        if 0<= new_row < N and 0<= new_col <N:
                            if copy_villages[new_row][new_col] !=0:
                                stack.append((new_row, new_col))
                                copy_villages[new_row][new_col] = 0  # 방문도장!
    cnt_list.append(cnt)

print(max(cnt_list))

