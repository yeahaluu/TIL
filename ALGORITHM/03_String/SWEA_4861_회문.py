import sys

sys.stdin = open('input_회문', 'r')

for tc in range(int(input())):
    # N*N 행렬에서 길이가 M인 회문 찾기
    N, M = map(int, input().split())
    arr = [[s for s in input()] for _ in range(N)]

    for x in range(N):
        for y in range(N - M + 1):
            row_count = 0
            col_count = 0
            for idx in range(M // 2):
                a = arr[y+idx][x]
                b = arr[y + M -1 - idx][x]

                c = y+idx
                d = y + M -1 - idx
                if arr[x][y+idx] == arr[x][y + M -1 - idx] or arr[y+idx][x] == arr[y + M -1 - idx][x]:
                    if arr[x][y+idx] == arr[x][y + M -1 - idx]:
                        row_count += 1
                        if row_count == M // 2:
                            print('#{} '.format(tc+1), end='')
                            print(''.join(arr[x][y:y+M]))
                            break
                    if arr[y+idx][x] == arr[y + M -1 - idx][x]:
                        col_count += 1
                        if col_count == M // 2:


                            print('#{} '.format(tc + 1), end='')
                            for i in range(y, y + M):
                                print(arr[i][x],end='')
                            break
                else:
                    break

# 행은 슬라이싱 불가!!!!!!!!!!!!!!!!!!!!!!!!
