dr = [0, 1]  # 오른쪽, 아래
dc = [1, 0]


def min_sum(row, col, s):
    global s_list, ans
    s += arr[row][col]
    if s > ans:  ##### 백트래킹!
        return
    for k in range(2):
        new_r = row + dr[k]
        new_c = col + dc[k]

        if new_r == N - 1 and new_c == N - 1:
            s += arr[new_r][new_c]
            ans = min(ans,s)
            s_list.append(ans)

        elif new_r < N and new_c < N:
            min_sum(new_r, new_c, s)


for tc in range(1, int(input()) + 1):
    N = int(input())
    arr = [[int(i) for i in input().split()] for _ in range(N)]
    ans= 250
    s_list = []
    s = 0
    min_sum(0, 0, s)


    print(f'#{tc} {min(s_list)}')

