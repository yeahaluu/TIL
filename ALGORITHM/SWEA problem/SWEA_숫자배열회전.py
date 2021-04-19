# 90도 회전하는 함수
# 처음 행을 마지막 열로보내는 것이 시작.
def rotation(mat, N):
    n_mat = [[0] * N for _ in range(N)]
    for c in range(N):
        for r in range(N):
            tmp = mat[c][r]
            n_mat[r][N - 1 - c] = tmp
    return n_mat

import sys

sys.stdin = open('input_숫자배열회전.txt', 'r')

for tc in range(1, int(input()) +1):
    N = int(input())
    mat = [list(map(int, input().split())) for _ in range(N)]

    rot1 = rotation(mat, N)
    rot2 = rotation(rot1, N)
    rot3 = rotation(rot2, N)
    print('#{}'.format(tc))
    for i in range(N):
        print("{} {} {}".format(''.join(map(str, rot1[i])), ''.join(map(str, rot2[i])), ''.join(map(str, rot3[i]))))