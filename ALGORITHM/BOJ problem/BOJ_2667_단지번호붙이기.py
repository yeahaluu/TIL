
dr = [-1, 1, 0, 0]  # 상하좌우
dc = [0, 0, -1, 1]

N = int(input())
town = [[int(i) for i in input()] for _ in range(N)]

stack = []
visited = town
cnt_lst = []

town_cnt = 0

for r in range(N):
    for c in range(N):
        if town[r][c] == 1:
            town_cnt+=1

while town_cnt:

    for r in range(N):
        for c in range(N):

            if town[r][c] == 1:
                cnt = 0
                stack.append((r, c))
                visited[r][c] = 0
                cnt += 1
                town_cnt -=1

                while stack:
                    element = stack.pop()
                    r = element[0]
                    c = element[1]

                    for k in range(4):
                        row = r + dr[k]
                        col = c + dc[k]

                        if 0 <= row <= N - 1 and 0 <= col <= N - 1:
                            if town[row][col] == 1:
                                stack.append((row, col))
                                visited[row][col] = 0
                                cnt += 1
                                town_cnt -=1

                cnt_lst.append(cnt)

cnt_lst.sort()
n = len(cnt_lst)
print(n)
for i in range(n):
    print(cnt_lst[i])